import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)

    list_values1 = [item["score"] * item["weight"] for item in json_data]
    return sum(list_values1)


print(f"{task():.3f}")
