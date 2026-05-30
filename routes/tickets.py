from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.ticket import Ticket
from schemas.ticket import TicketCreate, TicketUpdate, TicketResponse
from services.classifier import Classifier
from services.priority import PriorityAssigner
from services.responder import Responder
from typing import List

router = APIRouter()

classifier = Classifier()
priority_assigner = PriorityAssigner()
responder = Responder()

# Create a new ticket
@router.post("/tickets", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    category = classifier.classify(ticket.issue_description)
    priority = priority_assigner.assign(ticket.issue_description, category)
    response = responder.generate(category, priority)

    new_ticket = Ticket(
        customer_name=ticket.customer_name,
        issue_description=ticket.issue_description,
        category=category,
        priority=priority,
        response=response
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

# Get all tickets
@router.get("/tickets", response_model=List[TicketResponse])
def get_all_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()

# Get tickets by category
@router.get("/tickets/category/{category}", response_model=List[TicketResponse])
def get_by_category(category: str, db: Session = Depends(get_db)):
    tickets = db.query(Ticket).filter(Ticket.category == category).all()
    if not tickets:
        raise HTTPException(status_code=404, detail="No tickets found for this category")
    return tickets

# Get tickets by priority
@router.get("/tickets/priority/{priority}", response_model=List[TicketResponse])
def get_by_priority(priority: str, db: Session = Depends(get_db)):
    tickets = db.query(Ticket).filter(Ticket.priority == priority).all()
    if not tickets:
        raise HTTPException(status_code=404, detail="No tickets found for this priority")
    return tickets

# Update ticket status
@router.put("/tickets/{ticket_id}", response_model=TicketResponse)
def update_status(ticket_id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    existing = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Ticket not found")
    existing.status = ticket.status
    db.commit()
    db.refresh(existing)
    return existing

# Delete a ticket
@router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    existing = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(existing)
    db.commit()
    return {"message": "Ticket deleted successfully"}