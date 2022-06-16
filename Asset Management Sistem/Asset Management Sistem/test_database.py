import pytest
import database

import unittest


def test_connect():
    assert database.connect("data.db") != None
    assert database.connect("") == "Prazno"
    assert database.connect("alen.jk") == "Los format"

test_connect()  