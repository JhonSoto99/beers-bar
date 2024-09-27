from fastapi import APIRouter, Depends

from app.models.order import Order
from app.repositories.order_repository import OrderRepository
from app.repositories.stock_repository import StockRepository
from app.services.order_service import OrderService

router = APIRouter()


def get_order_service() -> OrderService:
    order_repository = OrderRepository()
    stock_repository = StockRepository()
    return OrderService(order_repository, stock_repository)


@router.get("/order", response_model=Order)
def get_order(order_service: OrderService = Depends(get_order_service)):
    """
    Retrieve the current order status.

    Args:
        order_service (OrderService): The service used to fetch the order.

    Returns:
        Order: The current order status.
    """
    return order_service.get_order_status()
