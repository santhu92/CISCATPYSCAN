import csv
import os
def write(results, host):
    os.makedirs("reports", exist_ok=True)
    with open(f"reports/{host}_report.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
