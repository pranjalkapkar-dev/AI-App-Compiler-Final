import time
import json

def run_eval(pipeline, dataset):

    results = []

    for item in dataset:

        start = time.time()

        try:
            output = pipeline(item["prompt"])
            status = "PASS"
        except:
            status = "FAIL"

        latency = time.time() - start

        results.append({
            "prompt": item["prompt"],
            "status": status,
            "latency": latency
        })

    print(json.dumps(results, indent=2))