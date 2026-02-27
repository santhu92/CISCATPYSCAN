def write(results, host):
    html = "<html><body><h2>Compliance Report</h2><table border=1>"
    html += "<tr><th>ID</th><th>Status</th><th>Description</th></tr>"

    for r in results:
        color = "green" if r["status"] == "PASS" else "red"
        html += f"<tr><td>{r['id']}</td><td style='color:{color}'>{r['status']}</td><td>{r['description']}</td></tr>"

    html += "</table></body></html>"

    with open(f"reports/{host}_report.html", "w") as f:
        f.write(html)
