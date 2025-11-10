from sqlalchemy.orm import Session
from collections import defaultdict
import models

def fetch_all_orders(db: Session):
    """
    Fetch all orders with item and payment details using SQLAlchemy ORM.
    """

    # Get distinct orders
    orders = (
        db.query(
            models.OrderHistory.order_id,
            models.OrderHistory.order_date,
            models.OrderHistory.order_status
        )
        .distinct()
        .all()
    )

    if not orders:
        return {"message": "No orders found", "data": []}

    # Fetch all order items
    all_items = (
        db.query(
            models.OrderHistory.order_id,
            models.OrderHistory.item_id,
            models.OrderHistory.size,
            models.OrderHistory.price,
            models.OrderHistory.qty,
            models.OrderHistory.total,
            models.Menu.item_name
        )
        .join(models.Menu, models.OrderHistory.item_id == models.Menu.item_id)
        .all()
    )

    # Fetch all payments
    all_payments = db.query(
        models.Payment.order_id,
        models.Payment.payment_id,
        models.Payment.payment_type,
        models.Payment.payment_status,
        models.Payment.total_paid,
        models.Payment.discount,
        models.Payment.tips
    ).all()

    # Group items by order
    items_by_order = defaultdict(list)
    for i in all_items:
        items_by_order[i.order_id].append({
            "item_id": i.item_id,
            "item_name": i.item_name,
            "size": i.size,
            "price": i.price,
            "qty": i.qty,
            "total": i.total
        })

    # Group payments by order
    payments_by_order = defaultdict(list)
    for p in all_payments:
        payments_by_order[p.order_id].append({
            "payment_id": p.payment_id,
            "payment_type": p.payment_type,
            "payment_status": p.payment_status,
            "total_paid": p.total_paid,
            "discount": p.discount,
            "tips": p.tips
        })

    # Build final response
    result = []
    for o in orders:
        order_id = o.order_id
        result.append({
            "order_id": order_id,
            "order_date": str(o.order_date),
            "status": o.order_status,
            "items": items_by_order.get(order_id, []),
            "payments": payments_by_order.get(order_id, [])
        })

    return {"total_orders": len(result), "data": result}

