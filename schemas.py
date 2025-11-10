from pydantic import BaseModel
from typing import List, Optional

class MenuItem(BaseModel):
    item_id: int
    item_name: str
    size: Optional[str]
    price: Optional[str]

    class Config:
        orm_mode = True

class OrderDetail(BaseModel):
    id: int
    order_date: str
    order_id: int
    size: Optional[str]
    price: float
    qty: int
    order_status: str
    total: float
    item: MenuItem

    class Config:
        orm_mode = True

class PaymentDetail(BaseModel):
    payment_id: int
    order_id: int
    total_paid: float
    payment_type: str
    payment_status: str

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    order_id: int
    items: List[OrderDetail]
    payments: List[PaymentDetail]
