import json


def generate(json_file, output):
    with open(json_file) as f:
        data = json.load(f)

    html = ""

    for finding in data["findings"]:
        html += f"""
<div class="card {finding['severity']}">
    <h2>{finding['title']}</h2>
    <p>Severity: {finding['severity']}</p>
    <pre>{finding['evidence']}</pre>
</div>
"""

    # Add security section
    security = data.get("security", {})

    html += f"""
<div class="card">
    <h2>Risk Score</h2>
    <pre>{security.get('risk')}</pre>
</div>

<div class="card">
    <h2>CVE Mapping</h2>
    <pre>{security.get('cve_mapping')}</pre>
</div>

<div class="card">
    <h2>Nuclei Findings</h2>
    <pre>{security.get('nuclei')}</pre>
</div>
"""

    with open("reports/templates/report.html") as f:
        template = f.read()

    final = template.replace("{{CONTENT}}", html)

    with open(output, "w") as f:
        f.write(final)

    print("[+] Report generated")
