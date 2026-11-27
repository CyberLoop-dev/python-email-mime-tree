from __future__ import annotations
import argparse
import json
import sys
from email import policy
from email.message import Message
from email.parser import BytesParser
from pathlib import Path
from typing import Any

def describe_part(part: Message, path: str = "1") -> dict[str, Any]:
    payload = part.get_payload(decode=True)
    raw_children = part.get_payload()
    children = []
    if part.is_multipart() and isinstance(raw_children, list):
        children = [
            describe_part(child, f"{path}.{index}")
            for index, child in enumerate(raw_children, 1)
            if isinstance(child, Message)
        ]
    return {
        "path": path,
        "content_type": part.get_content_type(),
        "disposition": part.get_content_disposition(),
        "filename": part.get_filename(),
        "charset": part.get_content_charset(),
        "decoded_bytes": len(payload) if payload is not None else None,
        "multipart": part.is_multipart(),
        "children": children,
    }

def summary(message: Message) -> dict[str, Any]:
    return {
        "subject": str(message.get("subject", "")),
        "from": str(message.get("from", "")),
        "to": str(message.get("to", "")),
        "parts": [describe_part(message)],
    }

def render(part: dict[str, Any], indent: str = "") -> list[str]:
    extras = []
    if part["disposition"]:
        extras.append(f"disposition={part['disposition']}")
    if part["filename"]:
        extras.append(f"filename={part['filename']!r}")
    if part["decoded_bytes"] is not None:
        extras.append(f"bytes={part['decoded_bytes']}")
    suffix = " " + " ".join(extras) if extras else ""
    lines = [f"{indent}{part['path']} {part['content_type']}{suffix}"]
    for child in part["children"]:
        lines.extend(render(child, indent + "  "))
    return lines

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Inspect a local .eml MIME tree without extracting parts.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--json", action="store_true", help="Print structured JSON")
    args = parser.parse_args(argv)
    try:
        with args.file.open("rb") as stream:
            message = BytesParser(policy=policy.default).parse(stream)
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    data = summary(message)
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(f"Subject: {data['subject'] or '(none)'}")
        print(f"From:    {data['from'] or '(none)'}")
        print(f"To:      {data['to'] or '(none)'}")
        print("MIME tree:")
        for root in data["parts"]:
            print("\n".join(render(root)))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
