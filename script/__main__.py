"""Allow running build_manifest as python -m build_manifest."""
from build_manifest import main

if __name__ == "__main__":
    raise SystemExit(main())
