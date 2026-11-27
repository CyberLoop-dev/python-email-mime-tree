import unittest
from email import policy
from email.parser import BytesParser
from email_mime_tree import describe_part, summary

class MimeTreeTests(unittest.TestCase):
    def test_nested_parts_and_attachment_metadata(self):
        raw = (
            b"Subject: sample\r\n"
            b"Content-Type: multipart/mixed; boundary=x\r\n\r\n"
            b"--x\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nhello\r\n"
            b"--x\r\nContent-Type: application/octet-stream\r\n"
            b"Content-Disposition: attachment; filename=sample.bin\r\n"
            b"Content-Transfer-Encoding: base64\r\n\r\naGVsbG8=\r\n--x--\r\n"
        )
        msg = BytesParser(policy=policy.default).parsebytes(raw)
        tree = describe_part(msg)
        self.assertEqual(len(tree["children"]), 2)
        self.assertEqual(tree["children"][1]["filename"], "sample.bin")
        self.assertEqual(tree["children"][1]["decoded_bytes"], 5)

    def test_summary_does_not_include_body_text(self):
        msg = BytesParser(policy=policy.default).parsebytes(
            b"Subject: private\r\nContent-Type: text/plain\r\n\r\nsecret body"
        )
        self.assertEqual(summary(msg)["subject"], "private")
        self.assertNotIn("secret body", str(summary(msg)))

if __name__ == "__main__":
    unittest.main()
