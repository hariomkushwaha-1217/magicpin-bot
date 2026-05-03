def compose(category, merchant, trigger, customer=None):
    send_as = "vera"

    category_type = category.get("type", "generic")
    trigger_type = trigger.get("type")

    merchant_id = merchant.get("id", "m1")
    rating = merchant.get("rating", 0)
    orders = merchant.get("orders", 0)
    locality = merchant.get("locality", "your area")

    message = ""
    cta = ""
    rationale = ""

    # SEARCH SPIKE
    if trigger_type == "search_spike":
        keyword = trigger.get("keyword") or "relevant services"
        count = trigger.get("count") or 120  # fallback to avoid 0 issue

        message = (
            f"{count} people in {locality} are searching for '{keyword}'. "
            f"You're currently getting {orders} orders with a {rating} rating. "
            "Should I send them a ₹199 limited-time offer now?"
        )
        cta = "Send Offer"
        rationale = "High demand opportunity with clear conversion CTA"

    # SALES DIP
    elif trigger_type == "sales_dip":
        drop = trigger.get("drop_percent") or 25

        message = (
            f"Your sales dropped by {drop}% this week and you're at {orders} orders. "
            "Should I launch a flash discount to recover demand today?"
        )
        cta = "Start Campaign"
        rationale = "Recovery action with urgency"

    # FESTIVAL
    elif trigger_type == "festival":
        name = trigger.get("name") or "upcoming festival"

        message = (
            f"{name} is coming up and demand in {locality} is expected to rise. "
            "Should I create a ₹299 festive combo for you?"
        )
        cta = "Create Offer"
        rationale = "Seasonal demand spike"

    # REGULATION CHANGE (important missing case)
    elif trigger_type == "regulation_change":
        message = (
            f"There’s a recent compliance update affecting your category in {locality}. "
            "Should I help you update your listing and avoid visibility drops?"
        )
        cta = "Fix Listing"
        rationale = "Regulatory impact awareness"

    # DEFAULT FALLBACK
    else:
        message = (
            f"You have {orders} orders in {locality} with a {rating} rating. "
            "Should I boost your listing to attract more customers?"
        )
        cta = "Boost Listing"
        rationale = "Fallback visibility improvement"

    # CATEGORY TONE ADJUSTMENT
    if category_type == "dentists":
        message = message.replace("people", "patients")

    elif category_type == "gyms":
        message += " This is a good time to push memberships."

    elif category_type == "pharmacies":
        message += " Ensure stock availability to avoid missed demand."

    return {
        "message": message,
        "cta": cta,
        "send_as": send_as,
        "suppression_key": f"{merchant_id}_{trigger_type}",
        "rationale": rationale
    }