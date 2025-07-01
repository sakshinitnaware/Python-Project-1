# Script to merge all the json reports and convert them to HTML reports

# Importing json and os library
import json
import os

# === 1. JSON report files ===
report_files = [
    r"F:\Assignments\python_code\project-1\Reports\firsttest_report.json",
    r"F:\Assignments\python_code\project-1\Reports\retest_report1.json",
    r"F:\Assignments\python_code\project-1\Reports\retest_report2.json",
    r"F:\Assignments\python_code\project-1\Reports\retest_report3.json",
    r"F:\Assignments\python_code\project-1\Reports\retest_report4.json"
]

# === 2. Output path ===
html_output_path = r"F:\Assignments\python_code\project-1\Reports\merged_final_report.html"

# === 3. Build testcase results from each trial ===
test_result_map = {}

for trial_index, file in enumerate(report_files, 1):
    with open(file, "r") as f:
        data = json.load(f)
        for test in data.get("tests", []):
            name = test["nodeid"]
            outcome = test["outcome"]
            if name not in test_result_map:
                test_result_map[name] = ["N/A"] * 5
            test_result_map[name][trial_index - 1] = outcome

# === 4. Determine summary: if passed at least once, it's Passed
summary_data = []
for test_name, results in test_result_map.items():
    if "passed" in results:
        final_result = "Passed"
    else:
        final_result = "Failed"
    summary_data.append((test_name, results, final_result))

# === 5. Generate HTML
html = f"""
<html>
<head>
    <title> Merged Test Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f9f9f9;
            padding: 20px;
        }}
        h1 {{
            color: #333;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: center;
        }}
        th {{
            background-color: #4CAF50;
            color: white;
        }}
        .passed {{
            background-color: #d4edda;
            color: #155724;
        }}
        .failed {{
            background-color: #f8d7da;
            color: #721c24;
        }}
        .na {{
            background-color: #f0f0f0;
            color: #999;
        }}
    </style>
</head>
<body>
    <h1> Merged Pytest Report (Trials 1–5)</h1>
    <table>
        <tr>
            <th>Test Case Name</th>
            <th>Trial 1</th>
            <th>Trial 2</th>
            <th>Trial 3</th>
            <th>Trial 4</th>
            <th>Trial 5</th>
            <th>Final Result</th>
        </tr>
"""

# === 6. Add each row for test case
for test_name, results, summary in summary_data:
    row = f"<tr><td>{test_name}</td>"
    for result in results:
        css = "passed" if result == "passed" else "failed" if result == "failed" else "na"
        row += f"<td class='{css}'>{result.title() if result != 'N/A' else 'N/A'}</td>"
    summary_class = "passed" if summary == "Passed" else "failed"
    row += f"<td class='{summary_class}'><strong>{summary}</strong></td></tr>"
    html += row

html += """
    </table>
</body>
</html>
"""

# === 7. Save HTML output
with open(html_output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML report saved to: {html_output_path}")
