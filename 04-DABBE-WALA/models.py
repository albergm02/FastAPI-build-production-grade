from enum import Enum
from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field

# Orderstatus (Enum) -> preparing, picked_up, in_transit, delivered
class OrderStatus(str, Enum):
    PREPARING = "preparing"
    PICKED_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"

# id (primary key)
# customer_name (str)
# delivery_address (str)
# items (str)
# status (OrderStatus)
# created_at
# updated_at

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_name: str
    delivery_address: str
    items: str
    status: OrderStatus = Field(default=OrderStatus.PREPARING)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": datetime.now(timezone.utc)})
# schema for creating a new order

class OrderCreate(SQLModel):
    customer_name: str
    delivery_address: str
    items: str

# schema for updating an order

class OrderUpdate(SQLModel):
    delivery_address: Optional[str] = None
    status: Optional[OrderStatus] = None

#status log

class OrderStatusLog(SQLModel):
    order_id: int
    old_status: str
    new_status: str
    changed_at: datetime