import yaml
from core.engine import ComplianceEngine

with open("config.yaml") as f:
    config = yaml.safe_load(f)

for target in config["targets"]:
    if target.get("mode") == "local":
        print(f"Scanning local machine ({target.get('os')})")
    else:
        print(f"Scanning {target.get('host')} ({target.get('os')})")

    engine = ComplianceEngine(target)
    engine.run()
    engine.generate_reports()
