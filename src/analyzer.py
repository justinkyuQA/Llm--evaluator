import json

def load_data(path="data/labeled.jsonl"):
    with open(path, "r") as f:
        return [json.loads(line) for line in f]

def summarize(data):
    scores = [d["score"] for d in data]
    return {
        "count": len(scores),
        "avg_score": sum(scores) / len(scores) if scores else 0
    }
