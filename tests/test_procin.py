#!/usr/bin/env python

"""Tests for `procin` package."""

import pytest


import procin


def test_array():
    c = procin.Command()
    ab = c.run_json(["echo", "-n", "[]"])
    assert ab == []

def test_pass():
    assert True
