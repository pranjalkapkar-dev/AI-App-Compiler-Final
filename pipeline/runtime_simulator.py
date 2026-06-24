def simulate_runtime(schema):

    return {
        "status": "success",
        "pages": len(schema["ui"]["pages"]),
        "apis": len(schema["api"]["endpoints"])
    }