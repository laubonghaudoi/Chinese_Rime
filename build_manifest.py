#!/usr/bin/env python3
"""Convenience entry point for running the manifest builder from the repo root.

The implementation lives in script/build_manifest.py so `python -m build_manifest`
continues to work from inside script/. This wrapper intentionally keeps the same
CLI available at the repository root, where site and workflow checks are usually
run.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCRIPT_DIR = ROOT / "script"
SCRIPT = SCRIPT_DIR / "build_manifest.py"

sys.path.insert(0, str(SCRIPT_DIR))

spec = importlib.util.spec_from_file_location("_chinese_rime_build_manifest", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load {SCRIPT}")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


if __name__ == "__main__":
    raise SystemExit(module.main())
