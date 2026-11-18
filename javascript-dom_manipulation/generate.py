#!/usr/bin/python3
import shutil
from pathlib import Path

# Find the highest existing index number
files = list(Path(".").glob("*-script.js"))

if not files:
    # First run: create the original HTML file
    number = 0

    content = """<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
"""

    Path("0-script.js").write_text(content)
    print("Created 0-script.js")

else:
    # Find the latest numbered file
    numbers = [
        int(f.name.split("-")[0])
        for f in files
        if f.name.split("-")[0].isdigit()
    ]

    latest = max(numbers)
    next_number = latest + 1

    source = Path(f"{latest}-script.js")
    destination = Path(f"{next_number}-script.js")

    # Copy the latest file into the next one
    shutil.copy2(source, destination)

    print(f"Copied {source} to {destination}")
