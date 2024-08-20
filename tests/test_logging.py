#!/usr/bin/env python

"""Tests for `litescript` package."""

from litescript import *  # noqa


def test_setup_logger():
    logger = setup_logger("test.log")
    logger.info("This is a test log message.")
    logger.error("This is an error log message.")
    logger.warning("This is a warning log message.")
    logger.debug("This is a debug log message.")
    logger.critical("This is a critical log message.")
    logger.exception("This is an exception log message.")
    assert Path("test.log").exists()
    assert Path("test.log").stat().st_size > 0
    os.remove("test.log")
    assert not Path("test.log").exists()
