def repair_output(schema, errors):

    if "auth" not in schema:
        schema["auth"] = {"roles": ["admin", "user"]}

    if "database" not in schema:
        schema["database"] = {"tables": []}

    # auto-fix missing API
    if "api" not in schema:
        schema["api"] = {"endpoints": []}

    return schema