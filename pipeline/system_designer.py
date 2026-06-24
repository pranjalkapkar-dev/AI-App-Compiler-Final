def design_system(intent):
    return {
        "entities": ["User", "Contact"],
        "roles": intent.get("roles", ["admin", "user"]),
        "flows": ["Login Flow", "Dashboard Flow"]
    }