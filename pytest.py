from __future__ import annotations

import sys
import unittest
from pathlib import Path


def path_to_module(path_arg: str) -> str:
    path = Path(path_arg)
    module_path = path.with_suffix("").as_posix().replace("/", ".")
    return module_path.lstrip(".")


def load_suite(args: list[str]) -> unittest.TestSuite:
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    test_targets = [arg for arg in args if not arg.startswith("-")]

    if not test_targets:
        return loader.discover("tests")

    for target in test_targets:
        path = Path(target)
        if path.exists():
            if path.is_dir():
                suite.addTests(loader.discover(str(path)))
            else:
                suite.addTests(loader.loadTestsFromName(path_to_module(target)))
        else:
            suite.addTests(loader.loadTestsFromName(target))

    return suite


def main() -> None:
    args = sys.argv[1:]
    verbosity = 1 if "-q" in args else 2
    suite = load_suite(args)
    result = unittest.TextTestRunner(verbosity=verbosity).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
