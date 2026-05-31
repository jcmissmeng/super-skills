import json
from pathlib import Path

import pytest

# Skill root directory (parent of tests/)
SKILL_ROOT = Path(__file__).parent.parent


@pytest.fixture
def skill_root():
    """Return the skill root directory path."""
    return SKILL_ROOT


@pytest.fixture
def skill_md(skill_root):
    """Return the content of SKILL.md."""
    return (skill_root / "SKILL.md").read_text(encoding="utf-8")


@pytest.fixture
def evals_data(skill_root):
    """Return the parsed evals.json data."""
    evals_path = skill_root / "evals" / "evals.json"
    return json.loads(evals_path.read_text(encoding="utf-8"))