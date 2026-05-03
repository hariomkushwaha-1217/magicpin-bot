@app.post("/v1/reply")
def reply(data: dict):
    message = data.get("message", "").lower()
    role = data.get("from_role", "merchant")

    # STOP / HOSTILE
    if any(word in message for word in ["stop", "spam", "don't", "do not"]):
        return {"action": "end"}

    # AUTO-REPLY
    if "thank you for contacting" in message:
        return {"action": "end"}

    # CUSTOMER RESPONSE (booking intent)
    if role == "customer":
        return {
            "action": "send",
            "body": "Your booking request is received. The merchant will confirm shortly.",
            "cta": "View Details"
        }

    # MERCHANT POSITIVE INTENT
    if any(word in message for word in ["yes", "ok", "sure", "do it", "go ahead"]):
        return {
            "action": "send",
            "body": "Great. I'm launching this campaign for you now. You should start seeing results shortly.",
            "cta": "View Campaign"
        }

    # MERCHANT QUESTION / HELP REQUEST
    if "help" in message or "what" in message:
        return {
            "action": "send",
            "body": "I can help you improve visibility, run offers, or recover sales. Would you like me to suggest the best option?",
            "cta": "Get Suggestions"
        }

    # DEFAULT
    return {
        "action": "send",
        "body": "Would you like me to run a campaign to improve your orders?",
        "cta": "Yes, proceed"
    }