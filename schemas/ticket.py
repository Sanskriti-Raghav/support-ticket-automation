from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TicketCreate(BaseModel):
    customer_name: str
    issue_description: str

class TicketUpdate(BaseModel):
    status: str

class TicketResponse(BaseModel):
    id: int
    customer_name: str
    issue_description: str
    category: str
    priority: str
    status: str
    response: str
    created_at: datetime

    class Config:
        from_attributes = True