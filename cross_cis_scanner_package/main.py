import os
import yaml
from core.engine import ComplianceEngine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(BASE_DIR, "config.yaml")

with open(config_path) as f:
    config = yaml.safe_load(f)

for target in config.get("targets", []):
    host = target.get("host", "local")
    platform = target.get("os", "unknown")

    if target.get("mode") == "local":
        print(f"\nScanning local machine ({platform})")
    else:
        print(f"\nScanning {host} ({platform})")

    try:
        engine = ComplianceEngine(target)
        engine.run()
        engine.generate_reports()
        print("Scan completed successfully.")
    except Exception as e:
        print(f"Error while scanning {host}: {str(e)}")
