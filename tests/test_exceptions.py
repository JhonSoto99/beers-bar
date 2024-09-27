import pytest

from app.repositories.exceptions import LoadOrderError, LoadStockError
from app.services.exceptions import InvalidOrderDataError


def test_load_order_error_default_message():
    with pytest.raises(LoadOrderError, match="Failed to load order data."):
        raise LoadOrderError()


def test_load_order_error_custom_message():
    custom_message = "Custom error loading order."
    with pytest.raises(LoadOrderError, match=custom_message):
        raise LoadOrderError(custom_message)


def test_load_stock_error_default_message():
    with pytest.raises(LoadStockError, match="Failed to load stock data."):
        raise LoadStockError()


def test_load_stock_error_custom_message():
    custom_message = "Custom error loading stock."
    with pytest.raises(LoadStockError, match=custom_message):
        raise LoadStockError(custom_message)


def test_invalid_order_data_error_default_message():
    with pytest.raises(
        InvalidOrderDataError, match="Invalid order data retrieved."
    ):
        raise InvalidOrderDataError()


def test_invalid_order_data_error_custom_message():
    custom_message = "Custom invalid order data error."
    error = InvalidOrderDataError(custom_message)
    assert str(error) == custom_message
