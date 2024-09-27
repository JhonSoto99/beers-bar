from unittest.mock import MagicMock

import pytest

from app.models.order import Item
from app.services.order_service import OrderService


@pytest.fixture
def mock_order_repository():
    return MagicMock()


@pytest.fixture
def mock_stock_repository():
    return MagicMock()


@pytest.fixture
def order_service(mock_order_repository, mock_stock_repository):
    return OrderService(mock_order_repository, mock_stock_repository)


def test_update_item_summary_new_item(order_service):
    item_summary = {}
    order_service.update_item_summary(item_summary, "Beer", 2, {"Beer": 5})

    assert "Beer" in item_summary
    assert item_summary["Beer"]["quantity"] == 2
    assert item_summary["Beer"]["price_per_unit"] == 5


def test_update_item_summary_existing_item(order_service):
    item_summary = {"Beer": {"quantity": 2, "price_per_unit": 5}}
    order_service.update_item_summary(item_summary, "Beer", 3, {"Beer": 5})

    assert item_summary["Beer"]["quantity"] == 5


def test_calculate_subtotal(order_service):
    items = [
        Item(name="Beer", price_per_unit=5, total=10),
        Item(name="Wine", price_per_unit=10, total=20),
    ]

    subtotal = order_service.calculate_subtotal(items)

    assert subtotal == 30
