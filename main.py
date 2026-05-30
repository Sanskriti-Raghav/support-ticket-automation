from fastapi import FastAPI
from database import Base, engine
from routes.tickets import router as ticket_router
import models.ticket

app = FastAPI(
    title="Customer Support Ticket Automation",
    description="A REST API to automate customer support ticket classification, priority assignment and response generation.",
    version="1.0.0"
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(ticket_router, prefix="/api/v1", tags=["Tickets"])

@app.get("/")
def root():
    return {"message": "Customer Support Ticket Automation API is running."}