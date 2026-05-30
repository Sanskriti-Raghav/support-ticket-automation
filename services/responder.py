class Responder:
    def generate(self, category: str, priority: str) -> str:
        responses = {
            "Billing": {
                "High": "Your billing issue has been escalated. Our team will contact you within 2 hours.",
                "Medium": "We have received your billing concern. Our team will resolve it within 24 hours.",
                "Low": "Thank you for your billing query. We will get back to you within 48 hours."
            },
            "Technical": {
                "High": "Critical technical issue detected. Our technical team is on it and will respond within 1 hour.",
                "Medium": "Your technical issue has been logged. Expected resolution within 24 hours.",
                "Low": "Thank you for reporting. Our team will look into it within 48 hours."
            },
            "Account": {
                "High": "Urgent account issue flagged. Our team will contact you within 2 hours.",
                "Medium": "Your account concern has been received. We will resolve it within 24 hours.",
                "Low": "Thank you for reaching out. Account query will be addressed within 48 hours."
            },
            "General": {
                "High": "Your request has been escalated and will be addressed within 2 hours.",
                "Medium": "Your request has been logged and will be addressed within 24 hours.",
                "Low": "Thank you for contacting us. We will get back to you within 48 hours."
            }
        }
        return responses[category][priority]