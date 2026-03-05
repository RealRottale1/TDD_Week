import pytest
from inventory import add_item, remove_item, get_item_count

@pytest.fixture
def empty_inventory():
    return {"items": [], "capacity": 10, "locked": False}

@pytest.fixture
def full_inventory():
    return {"items": ["a"] * 10, "capacity": 10, "locked": False}

@pytest.fixture
def locked_inventory():
    return {"items": ["sword"], "capacity": 10, "locked": True}

def test_add_item_empty():
    inventory = empty_inventory()
    item = "item"
    assert item in add_item(inventory, item)["items"] == True