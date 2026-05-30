# support-ticket-automation
# Customer Support Ticket Automation

A REST API-based automation tool built with Python and FastAPI that processes customer support tickets by automatically classifying them by type, assigning priority levels, and generating appropriate responses.

## Features

- Auto-classify tickets by category — Billing, Technical, Account, General
- Auto-assign priority — High, Medium, Low based on issue keywords
- Auto-generate response message based on category and priority
- View all tickets
- Filter tickets by category or priority
- Update ticket status — Open, In Progress, Resolved
- Delete a ticket
- Interactive API documentation via Swagger UI

## Tech Stack

- **Python 3.12**
- **FastAPI** — REST API framework
- **MySQL** — Database
- **SQLAlchemy** — ORM
- **Uvicorn** — ASGI server

## Project Structure

```
support-ticket-automation/
├── models/
│   └── ticket.py        # Database model
├── routes/
│   └── tickets.py       # API endpoints
├── services/
│   ├── classifier.py    # Ticket classification logic
│   ├── priority.py      # Priority assignment logic
│   └── responder.py     # Response generation logic
├── schemas/
│   └── ticket.py        # Request/response schemas
├── main.py              # App entry point
├── database.py          # Database connection
├── requirements.txt
└── .env                 # Environment variables
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Sanskriti-Raghav/support-ticket-automation.git
cd support-ticket-automation
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the root directory:
```
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost:3306/support_tickets
```

### 5. Create MySQL database
```sql
CREATE DATABASE support_tickets;
```

### 6. Run the application
```bash
uvicorn main:app --reload
```

### 7. Access Swagger UI
```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/v1/tickets | Create a new ticket |
| GET | /api/v1/tickets | Get all tickets |
| GET | /api/v1/tickets/category/{category} | Filter by category |
| GET | /api/v1/tickets/priority/{priority} | Filter by priority |
| PUT | /api/v1/tickets/{ticket_id} | Update ticket status |
| DELETE | /api/v1/tickets/{ticket_id} | Delete a ticket |

## Example Request

```json
POST /api/v1/tickets
{
  "customer_name": "John Doe",
  "issue_description": "My payment is not going through and I got charged twice"
}
```

## Example Response

```json
{
  "id": 1,
  "customer_name": "John Doe",
  "issue_description": "My payment is not going through and I got charged twice",
  "category": "Billing",
  "priority": "Medium",
  "status": "Open",
  "response": "We have received your billing concern. Our team will resolve it within 24 hours.",
  "created_at": "2026-05-31T02:20:39"
}
```
