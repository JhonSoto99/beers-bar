from typing import Dict

from pydantic import ValidationError

from app.models.stock import Stock
from data.stock_data import mock_stock_data


class StockRepository:
    """
    Repository class for handling stock data.

    This class is responsible for loading and retrieving stock information.
    In this case, it uses mock data to simulate a database.
    """

    def __init__(self):
        """
        Initializes the StockRepository.

        Loads the stock data from the provided mock data.
        """
        self.stock = self._load_stock(mock_stock_data)

    def _load_stock(self, stock_data: Dict) -> Stock:
        """
        Loads a Stock object from a dictionary of stock data.

        Args:
            stock_data (Dict): A dictionary representing the stock data.

        Returns:
            Stock: An instance of the Stock model with the loaded data.
        """
        try:
            return Stock(**stock_data)
        except ValidationError as e:
            print(f"Failed to load order data: {e}")
            raise

    def get_stock(self) -> Stock:
        """
        Retrieves the current stock.

        Returns:
            Stock: The current loaded stock.
        """
        return self.stock
