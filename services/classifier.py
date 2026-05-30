class Classifier:
    def classify(self, issue_description: str) -> str:
        issue = issue_description.lower()

        billing_keywords = ["bill", "payment", "charge", "invoice", "refund", "amount", "due", "transaction"]
        technical_keywords = ["error", "not working", "down", "slow", "crash", "bug", "issue", "connect", "login"]
        account_keywords = ["account", "password", "username", "profile", "access", "locked", "reset", "register"]

        if any(word in issue for word in billing_keywords):
            return "Billing"
        elif any(word in issue for word in technical_keywords):
            return "Technical"
        elif any(word in issue for word in account_keywords):
            return "Account"
        else:
            return "General"