from jsonschema import validate

schema_contract = {
    "type": "object",
    "required": ["ui", "api", "database", "auth"]
}

def validate_output(output):
    try:
        validate(instance=output, schema=schema_contract)
        return {"valid": True}
    except Exception as e:
        return {"valid": False, "errors": str(e)}

def cross_validate(schema):

    errors = []

    db_tables = {t["name"] for t in schema["database"]["tables"]}

    api_paths = {e["path"] for e in schema["api"]["endpoints"]}

    ui_pages = set(schema["ui"]["pages"])

    if "contacts" in ui_pages and "/contacts" not in api_paths:
        errors.append("UI page missing API endpoint: contacts")

    return errors