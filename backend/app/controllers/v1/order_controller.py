from fastapi import APIRouter, Depends, status

from backend.app.models.order import Order
from backend.app.repositories.order_repository import OrderRepository
from backend.app.repositories.stock_repository import StockRepository
from backend.app.services.order_service import OrderService

router = APIRouter()


def get_order_service() -> OrderService:
    """
    Create and retrieve an instance of OrderService.

    This function initializes the OrderRepository and StockRepository,
    and returns an instance of OrderService that can be used to handle
    order-related operations.

    Returns:
        OrderService: An instance of the OrderService class, configured
        with the necessary repositories for order and stock management.
    """
    order_repository = OrderRepository()
    stock_repository = StockRepository()
    return OrderService(order_repository, stock_repository)


@router.get(
    "/order",
    response_model=Order,
    status_code=status.HTTP_200_OK,
    tags=["Orders"],
    responses={
        200: {
            "description": "Successful Response.",
            "content": {
                "application/json": {
                    "example": {
                        "created": "2024-09-10T12:00:00",
                        "paid": False,
                        "subtotal": 1050,
                        "taxes": 0,
                        "discounts": 0,
                        "items": [
                            {
                                "name": "Quilmes",
                                "price_per_unit": 120,
                                "total": 600,
                            }
                        ],
                        "rounds": [
                            {
                                "created": "2024-09-10T12:00:30",
                                "items": [
                                    {"name": "Corona", "quantity": 2},
                                    {"name": "Club Colombia", "quantity": 1},
                                ],
                            },
                        ],
                    }
                }
            },
        },
        422: {
            "description": "Unprocessable Entity.",
            "content": {
                "application/json": {
                    "example": {"message": "Order is None or has no rounds."}
                }
            },
        },
        500: {
            "description": "Internal Server Error. Please try again later.",
            "content": {
                "application/json": {"example": {"message": "Data error"}}
            },
        },
    },
)
def get_order(order_service: OrderService = Depends(get_order_service)):
    """
    Retrieve the current order status.

    **Responses:**
    - **204**: Created successfully.
    - **422**: Invalid data submitted.
    - **500**: Internal server error.


    **Example Successful Response (200):**
    ```json
    {
        "created": "2024-09-10T12:00:00",
        "paid": False,
        "subtotal": 1050,
        "taxes": 0,
        "discounts": 0,
        "items": [
            {
                "name": "Quilmes",
                "price_per_unit": 120,
                "total": 600
            }
        ],
        "rounds": [
            {
                "created": "2024-09-10T12:00:30",
                "items": [
                    {
                        "name": "Corona",
                        "quantity": 2
                    },
                    {
                        "name": "Club Colombia",
                        "quantity": 1
                    }
                ]
            },
        ]
    }
    ```

    **Example Unprocessable Entity (422):**
    ```json
    {
      "message": "Order is None or has no rounds."
    }
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
    return order_service.get_order_status()
