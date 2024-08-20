from litescript.data_science import * # noqa

def test_exports():
    assert {
    "np",
    "pd",
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
    } < set(globals())