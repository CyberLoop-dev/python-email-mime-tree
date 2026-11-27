<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=170&section=header&text=Email%20MIME%20Tree&fontSize=34&fontColor=ffffff&animation=twinkling)

[![Typing](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=19&pause=1000&color=14B8A6&center=true&vCenter=true&width=650&lines=Small+tool%2C+clear+insight;Local-first+%E2%80%A2+Beginner-friendly)](https://git.io/typing-svg)

![License](https://img.shields.io/github/license/CyberLoop-dev/python-email-mime-tree)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/python-email-mime-tree)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/python-email-mime-tree)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/python-email-mime-tree)

![Project mark](assets/mark.svg)

</div>

## 📖 Overview

A read-only CLI for inspecting saved RFC-style `.eml` messages. It reports nested MIME structure, content types, dispositions, filenames, character sets, and decoded payload sizes. It never extracts attachments or contacts a mail server.

## ✨ Features

- 🧩 Walk nested multipart messages and show each part's path
- 📎 Report attachment metadata without writing attachments to disk
- 📏 Show decoded payload sizes and declared character sets
- 🧾 Export structured JSON for scripts
- 🔒 Read local files only; message bodies are not printed by default

## 🖥️ Demo

No hosted demo is claimed. Run the project locally using the steps below.

## 🚀 Quick Start

```bash
python -m pip install -e .
email-mime-tree sample.eml
email-mime-tree sample.eml --json
```

## 🧰 Tech Stack

Python 3.10+ standard library (`email`, `argparse`, `json`); `unittest`.

## 🗂️ Folder Structure

```text
python-email-mime-tree/
├── email_mime_tree.py
├── tests/test_email_mime_tree.py
├── assets/mark.svg
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

## 🗺️ Roadmap

- [ ] Add more edge-case examples
- [ ] Improve machine-readable output and documentation
- [ ] Expand the automated test fixtures

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, document behavior, and add a regression test for each bug fix.

## 📄 License

Released under the [MIT License](LICENSE).

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer&animation=twinkling)

</div>
