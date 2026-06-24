def generate_schema(architecture):
    return {
        "ui": {
            "pages": ["Login", "Dashboard"]
        },
        "api": {
            "endpoints": [
                {"path": "/login", "method": "POST"}
            ]
        },
        "database": {
            "tables": [
                {
                    "name": "users",
                    "columns": ["id", "email", "password"]
                }
            ]
        },
        "auth": {
            "roles": architecture["roles"]
        }
    }