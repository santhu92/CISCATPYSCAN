import re

def evaluate(expected, output):
    numbers = re.findall(r"\d+", output)
    if not numbers:
        return "FAIL"

    value = int(numbers[-1])

    if expected.startswith(">="):
        return "PASS" if value >= int(expected[2:]) else "FAIL"
    elif expected.startswith("<="):
        return "PASS" if value <= int(expected[2:]) else "FAIL"

    return "FAIL"
