from uuid import UUID
from typing import Optional
from datetime import datetime

class Invoice:
    def __init__(self, id: UUID, customer_id: UUID, invoice_id: str, payment_id: Optional[UUID], amount: float, tax: float,
                 total_amount: float, subscription: str, subscription_id: UUID, status: str,
                 created_at: datetime, updated_at: datetime, generation_date: datetime, period: datetime):
        self.id = id
        self.customer_id = customer_id
        self.invoice_id = invoice_id
        self.payment_id = payment_id
        self.amount = amount
        self.tax = tax
        self.total_amount = total_amount
        self.subscription = subscription
        self.subscription_id = subscription_id
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.generation_date = generation_date
        self.period = period