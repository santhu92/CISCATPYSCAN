import os
import yaml
from core.executor import execute
from core.evaluator import evaluate
from output import txt_writer, csv_writer, xml_writer, html_writer


class ComplianceEngine:
    def __init__(self, target):
        self.target = target
        self.results = []
        self.platform = target.get("os") or target.get("platform")
        self.host = target.get("host", "local")

    def run(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        rules_path = os.path.join(os.path.dirname(base_dir), "rules.yaml")

        with open(rules_path) as f:
            rules = yaml.safe_load(f)

        for rule in rules:
            rule_platform = rule.get("platform")

            # Skip rule if platform mismatch
            if rule_platform and rule_platform != self.platform:
                continue

            try:
                output = execute(self.target, rule.get("command"))
                status = evaluate(rule.get("expected"), output)

                self.results.append({
                    "id": rule.get("id"),
                    "description": rule.get("description"),
                    "status": status,
                    "severity": rule.get("severity"),
                    "output": output.strip()
                })

            except Exception as e:
                self.results.append({
                    "id": rule.get("id"),
                    "description": rule.get("description"),
                    "status": "ERROR",
                    "severity": rule.get("severity"),
                    "output": str(e)
                })

    def generate_reports(self):
        if not self.results:
            print("No results to generate reports.")
            return

        txt_writer.write(self.results, self.host)
        csv_writer.write(self.results, self.host)
        xml_writer.write(self.results, self.host)
        html_writer.write(self.results, self.host)

        print("Reports generated successfully.")
