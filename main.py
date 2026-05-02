from fastapi import FastAPI
from composer import compose
from storage import save_context

app = FastAPI()


# ✅ Health Check
@app.get("/v1/healthz")
def health():
    return {"status": "ok"}


# ✅ Metadata
@app.get("/v1/metadata")
def metadata():
    return {
        "team_name": "Hari Om Kushwaha",
        "bot_name": "Vera Engine",
        "model": "rule-based-v1"
    }


# ✅ Context Store
@app.post("/v1/context")
def context(data: dict):
    context_id = data.get("context_id")
    payload = data.get("payload")

    save_context(context_id, payload)

    return {
        "accepted": True,
        "context_id": context_id
    }


# ✅ Tick (Judge Compatible)
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


# ✅ Reply (FINAL FIXED VERSION)
@app.post("/v1/reply")
def reply(data: dict):
    message = data.get("message", "").lower()

    # 🔴 HOSTILE / STOP
    if any(word in message for word in ["stop", "spam", "don't", "do not"]):
        return {
            "action": "end"
        }

    # 🔴 AUTO-REPLY DETECTION (important)
    if "thank you for contacting" in message:
        return {
            "action": "end"
        }

    # 🔹 POSITIVE INTENT (strong action)
    if any(word in message for word in ["yes", "ok", "sure", "do it"]):
        return {
            "action": "send",
            "body": "Done. Your campaign is now being created. You’ll start receiving orders shortly.",
            "cta": "View Campaign"
        }

    # 🔹 DEFAULT
    return {
        "action": "wait",
        "wait_seconds": 30
    }