import xml.etree.ElementTree as ET

def write(results, host):
    root = ET.Element("ComplianceReport")

    for r in results:
        rule = ET.SubElement(root, "Rule")
        for k, v in r.items():
            ET.SubElement(rule, k).text = str(v)

    tree = ET.ElementTree(root)
    tree.write(f"reports/{host}_report.xml")
