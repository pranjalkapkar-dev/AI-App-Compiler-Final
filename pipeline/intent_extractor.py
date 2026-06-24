def extract_intent(prompt):
    prompt_lower = prompt.lower()

    modules = []
    roles = ["admin", "user"]
    business_features = []

    # Detect modules
    if "login" in prompt_lower:
        modules.append("login")

    if "dashboard" in prompt_lower:
        modules.append("dashboard")

    if "contact" in prompt_lower:
        modules.append("contacts")

    if "payment" in prompt_lower:
        modules.append("payments")

    if "analytics" in prompt_lower:
        modules.append("analytics")

    if "product" in prompt_lower:
        modules.append("products")

    if "cart" in prompt_lower:
        modules.append("cart")

    if "seller" in prompt_lower:
        roles.append("seller")

    if "customer" in prompt_lower:
        roles.append("customer")

    business_features = modules.copy()

    return {
        "app_name": "Generated Application",
        "modules": modules,
        "roles": list(set(roles)),
        "business_features": business_features
    }