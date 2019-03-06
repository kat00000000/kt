import item
import pytest

def test_item_init():
    assert item.Item(10).item_count_get() == 10

def test_item_init2():
    assert item.Item("a").item_count_get() == 10
