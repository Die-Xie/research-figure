"""Basic integrity checks for the distributable skill."""

import re
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "research-figure"


class SkillIntegrityTests(unittest.TestCase):
    def test_required_files_and_metadata(self):
        source = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(source, r"(?m)^name: research-figure$")
        self.assertRegex(source, r"(?m)^description: .+")
        self.assertTrue((SKILL / "agents" / "openai.yaml").is_file())

    def test_relative_markdown_links_exist(self):
        for document in SKILL.rglob("*.md"):
            content = document.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)]+)\)", content):
                target = target.split("#", 1)[0]
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                with self.subTest(document=document, target=target):
                    self.assertTrue((document.parent / unquote(target)).exists())


if __name__ == "__main__":
    unittest.main()
