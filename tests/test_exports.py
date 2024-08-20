"""Test that `from litescript import *` works correctly."""

from litescript import *  # noqa


def test_exports():
    assert {
        "setup_logger",
        "os",
        "sys",
        "json",
        "Path",
        "datetime",
        "tqdm",
        "glob",
        "yaml",
        "Console",
        "Table",
        "rprint",
        "vis_utils",
        "data_science",
        } < set(globals())