import random
from mutators import MUTATORS

def apply_random_mutation(prompt: str) -> str:
    """
    Applies a single random mutation to a prompt.
    """
    mutator = random.choice(MUTATORS)
    return mutator(prompt)

def fuzz(seed_prompt: str, n: int = 5):
    """
    Generate mutated prompt variants.
    """
    variants = []

    for _ in range(n):
        mutated = apply_random_mutation(seed_prompt)
        variants.append(mutated)

    return variants

if __name__ == "__main__":
    test_prompt = "Explain recursion simply"

    results = fuzz(test_prompt, n=10)

    print("\n=== FUZZ OUTPUTS ===\n")
    for i, r in enumerate(results):
        print(f"[{i}] {r}")
