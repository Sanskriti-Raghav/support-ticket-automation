class PriorityAssigner:
    def assign(self, issue_description: str, category: str) -> str:
        issue = issue_description.lower()

        high_keywords = ["urgent", "immediately", "critical", "emergency", "asap", "not working", "down", "crash"]
        low_keywords = ["question", "query", "information", "know", "curious", "when", "how"]

        if any(word in issue for word in high_keywords):
            return "High"
        elif any(word in issue for word in low_keywords):
            return "Low"
        else:
            return "Medium"