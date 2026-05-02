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

    # 🔹 SEARCH SPIKE (High scoring logic)
    if trigger_type == "search_spike":
        keyword = trigger.get("keyword", "")
        count = trigger.get("count", 0)

        if orders < 20:
            message = (
                f"{count} people in {locality} are searching for '{keyword}', but you're getting only {orders} orders. "
                "Capture this demand now with a ₹199 limited-time offer."
            )
            rationale = "High demand but low conversion → aggressive push"

        elif rating >= 4.5:
            message = (
                f"{count} people are searching for '{keyword}' in {locality}. "
                f"Your strong rating ({rating}) gives you an edge. Launch a premium combo to maximize revenue."
            )
            rationale = "High rating → premium positioning"

        else:
            message = (
                f"{count} people are searching for '{keyword}' near {locality}. "
                "Boost conversions with a ₹199 offer."
            )
            rationale = "Moderate performance → improve conversion"

        cta = "Send Offer"

    # 🔹 SALES DIP
    elif trigger_type == "sales_dip":
        drop = trigger.get("drop_percent", 0)

        message = (
            f"Your sales dropped by {drop}% and you currently have {orders} orders. "
            "Recover demand with a flash discount campaign today."
        )
        cta = "Start Campaign"
        rationale = "Sales drop → recovery needed"

    # 🔹 FESTIVAL
    elif trigger_type == "festival":
        name = trigger.get("name", "Upcoming festival")

        message = (
            f"{name} is approaching and demand in {locality} will spike. "
            "Launch a ₹299 festive combo to attract more customers."
        )
        cta = "Create Offer"
        rationale = "Seasonal spike opportunity"

    # 🔹 CATEGORY TONE ADJUSTMENT
    if category_type == "dentists":
        message = message.replace("people", "patients")

    elif category_type == "gyms":
        message += " Push memberships while demand is high."

    elif category_type == "pharmacies":
        message += " Ensure stock availability to avoid missed sales."

    # 🔹 DEFAULT FALLBACK
    if not message:
        message = (
            f"You currently have {orders} orders in {locality}. "
            "Increase visibility to attract more customers."
        )
        cta = "Boost Listing"
        rationale = "Fallback visibility"

    return {
        "message": message,
        "cta": cta,
        "send_as": send_as,
        "suppression_key": f"{merchant_id}_{trigger_type}",
        "rationale": rationale
    }