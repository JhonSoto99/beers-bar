from backend.app.base_exceptions import CustomError


class InvalidOrderDataError(CustomError):
    def __init__(self, message: str = "Invalid order data retrieved."):
        self.message = message

    def __str__(self) -> str:
        return self.message
