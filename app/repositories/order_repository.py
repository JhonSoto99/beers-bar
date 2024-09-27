from typing import Dict

from pydantic import ValidationError

from app.models.order import Order
from app.repositories.exceptions import LoadOrderError
from data.order_data import mock_order_data


class OrderRepository:
    """
    Repository class for handling order data.

    This class is responsible for loading and retrieving order information.
    In this case, it uses mock data to simulate the database.
    """

    def __init__(self):
        """
        Initializes the OrderRepository.

        Loads the order data from the provided mock data.
        """
        self.order: Order = self._load_order(mock_order_data)

    def _load_order(self, order_data: Dict) -> Order:
        """
        Loads an Order object from a dictionary of order data.

        Args:
            order_data (Dict): A dictionary representing the order data.

        Returns:
            Order: An instance of the Order model with the loaded data.

        Raises:
            LoadOrderError: Failed to load order data.
        """
        try:
            return Order(**order_data)
        except ValidationError as e:
            raise LoadOrderError(f"Validation failed: {e}") from e

    def get_order(self) -> Order:
        """
        Retrieves the current order.

        Returns:
            Order: The current loaded order.
        """
        return self.order
