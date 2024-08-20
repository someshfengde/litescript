from litescript.vis_utils import *


def test_exports():
    assert {"plt", "px"} < set(globals())
