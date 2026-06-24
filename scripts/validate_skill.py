from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "references/workflow-three-layers.md",
    "references/responsibility-complete-not-complex.md",
    "references/module-contract-rules.md",
    "references/change-impact-rules.md",
    "references/wizard-flow.md",
    "references/ui-language-rules.md",
    "references/ui-style-guide.md",
    "references/intake-template.md",
    "references/feature-menus.md",
    "references/complexity-rubric.md",
    "references/tech-stack-guide.md",
    "references/llm-integration-rules.md",
    "references/run-check-policy.md",
    "references/architecture-rules.md",
    "templates/confirmation-draft.md",
    "templates/llm-development-design-package.md",
    "templates/stage-prompt.md",
    "examples/resume-rewriter.md",
    "examples/document-summarizer.md",
    "examples/contract-analyzer.md",
    "docs/INSTALL.md",
    "docs/USAGE.md",
    "docs/NAMING.md",
    "tests/smoke-test-prompts.md",
]

def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)

def main() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            fail(f"Missing required file: {rel}")
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter.")
    m = re.match(r"^---\n(.*?)\n---\n", skill, flags=re.S)
    if not m:
        fail("SKILL.md frontmatter is not closed correctly.")
    frontmatter = m.group(1)
    if not re.search(r"^name:\s*archpilot\s*$", frontmatter, flags=re.M):
        fail("SKILL.md frontmatter must include name: archpilot")
    desc_match = re.search(r"^description:\s*(.+)$", frontmatter, flags=re.M)
    if not desc_match:
        fail("SKILL.md frontmatter must include description.")
    if len(desc_match.group(1).strip()) < 120:
        fail("Description is too short for ArchPilot activation.")
    required_phrases = [
        "ArchPilot",
        "LLM-executable architecture designer",
        "责任完整，不是技术复杂",
        "Requirement translation layer",
        "Architecture design layer",
        "LLM execution layer",
        "Every core module",
        "no mock",
        "run checks",
    ]
    skill_lower = skill.lower()
    for phrase in required_phrases:
        if phrase.lower() not in skill_lower:
            fail(f"SKILL.md should mention: {phrase}")
    print("OK: skill package structure is valid.")

if __name__ == "__main__":
    main()
