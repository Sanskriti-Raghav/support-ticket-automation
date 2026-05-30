from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)
    issue_description = Column(String(500), nullable=False)
    category = Column(String(50))        # Billing, Technical, Account
    priority = Column(String(20))        # High, Medium, Low
    status = Column(String(20), default="Open")  # Open, In Progress, Resolved
    response = Column(String(500))
    created_at = Column(DateTime, default=func.now())