"""Shared pytest fixtures for manifest builder tests."""
from pathlib import Path
import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture
def sources_dir(fixtures_dir: Path) -> Path:
    return fixtures_dir / "sources"
