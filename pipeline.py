import json
import os

from src.fuzzer import fuzz
from src.runner import mock_llm
from src.evaluator import evaluate

OUTPUT_FILE = "data/final_results.jsonl"

def run_pipeline(seed_prompt: str, n: int = 5):
    # ensure output directory exists
    os.makedirs("data", exist_ok=True)

    # 1. generate prompt variants
    variants = fuzz(seed_prompt, n)

    print(f"[PIPELINE] Generated {len(variants)} variants")

    for i, prompt in enumerate(variants):
        # 2. run model (mock)
        result = mock_llm(prompt)

        # 3. evaluate output
        evaluation = evaluate({
            "input": prompt,
            "output": result["output"]
        })

        # 4. combine record
        record = {
            "input": prompt,
            "output": result["output"],
            "score": evaluation["score"],
            "analysis": evaluation["analysis"]
        }

        # 5. persist (JSONL)
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

        print(f"[{i}] score={evaluation['score']}")

    print("[PIPELINE] Complete")

if __name__ == "__main__":
    seed = "Explain recursion simply"
    run_pipeline(seed, n=8)
