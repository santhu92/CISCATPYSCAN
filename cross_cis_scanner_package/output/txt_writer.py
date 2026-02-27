import os
def write(results, host):
    os.makedirs("reports", exist_ok=True)
    with open(f"reports/{host}_report.txt", "w") as f:
        for r in results:
            f.write(f"{r['id']} | {r['status']} | {r['description']}\n")
