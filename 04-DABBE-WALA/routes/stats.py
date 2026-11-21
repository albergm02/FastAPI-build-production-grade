from datetime import datetime, date, timezone
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, func
from models import Order, OrderStatus
from database import get_session

router = APIRouter(prefix="/stats", tags=["stats"])

@router.get("/daily")
def daily_summary(
    summary_date: date | None = Query(None, description="Date for the summary (YYYY-MM-DD)"),
    session: Session = Depends(get_session)
):
    if summary_date is None:
        summary_date = date.today()

    start = datetime.combine(summary_date, datetime.min.time(), tzinfo=timezone.utc)
    end = datetime.combine(summary_date, datetime.max.time(), tzinfo=timezone.utc)
    
    summary = {}
    total = 0

    for status in OrderStatus:
        count = session.exec(
            select(func.count())
            .where(Order.status == status)
            .where(Order.created_at >= start, Order.created_at <= end)
        ).one()
        summary[status.value] = count
        total += count

    return {
        "date": summary_date.isoformat(),
        "total_orders": total,
        "by_status": summary
    }

