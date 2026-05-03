from fastapi import FastAPI
from composer import compose
from storage import save_context

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Vera Message Engine is running",
        "status": "ok"
    }


@app.get("/v1/healthz")
def health():
    return {"status": "ok"}


@app.get("/v1/metadata")
def metadata():
    return {
        "team_name": "Hari Om Kushwaha",
        "bot_name": "Vera Engine",
        "model": "rule-based-v1"
    }


@app.post("/v1/context")
def context(data: dict):
    context_id = data.get("context_id")
    payload = data.get("payload")

    save_context(context_id, payload)

    return {
        "accepted": True,
        "context_id": context_id
    }


@app.post("/v1/tick")
def tick(data: dict):
    triggers = data.get("available_triggers", [])
    actions = []

    for trig_id in triggers:
        merchant = {
            "id": "m1",
            "rating": 4.2,
            "orders": 15
        }

        category = {"type": "restaurant"}

        result = compose(category, merchant, {"type": "search_spike"}, None)

        actions.append({
            "type": "message",
            "body": result["message"],
            "cta": result["cta"],
            "send_as": result["send_as"],
            "merchant_id": merchant["id"],
            "trigger_id": trig_id
        })

    return {"actions": actions}


@app.post("/v1/reply")
def reply(data: dict):
    message = data.get("message", "").lower()
    role = data.get("from_role", "merchant")

    if any(word in message for word in ["stop", "spam", "don't", "do not"]):
        return {"action": "end"}

    if "thank you for contacting" in message:
        return {"action": "end"}

    if role == "customer":
        return {
            "action": "send",
            "body": "Your booking request is received. The merchant will confirm shortly.",
            "cta": "View Details"
        }

    if any(word in message for word in ["yes", "ok", "sure", "do it", "go ahead"]):
        return {
            "action": "send",
            "body": "Great. I'm launching this campaign for you now.",
            "cta": "View Campaign"
        }

    return {
        "action": "send",
        "body": "Would you like me to run a campaign to improve your orders?",
        "cta": "Yes, proceed"
    }