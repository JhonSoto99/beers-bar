from backend.app.base_exceptions import CustomError


class LoadOrderError(CustomError):
    def __init__(self, message: str = "Failed to load order data.", *args):
        super().__init__(message, *args)

    def __str__(self) -> str:
        return self.args[0]


class LoadStockError(CustomError):
    def __init__(self, message: str = "Failed to load stock data.", *args):
        super().__init__(message, *args)

    def __str__(self) -> str:
        return self.args[0]
