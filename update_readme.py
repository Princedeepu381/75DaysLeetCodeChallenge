import os
import re

# Updated to use the 'main' branch
REPO_URL = "https://github.com/Princedeepu381/75DaysLeetCodeChallenge/tree/main/"
README_PATH = "README.md"

TOPICS_MAP = {
    "0001": "`Array`, `Hash Table`",
    "0026": "`Array`, `Two Pointers`",
    "0049": "`Array`, `Hash Table`, `Sorting`, `String`",
    "0125": "`String`, `Two Pointers`",
    "0217": "`Array`, `Hash Table`, `Sorting`",
    "0238": "`Array`, `Prefix Sum`",
    "0242": "`Hash Table`, `Sorting`, `String`",
    "0347": "`Array`, `Hash Table`, `Sorting`, `Heap`, `Bucket Sort`",
    "0448": "`Array`, `Hash Table`"
}

def format_name(folder_name):
    parts = folder_name.split('-')
    num = parts[0]
    name = ' '.join(parts[1:]).title()
    return num, name

folders = [f for f in os.listdir('.') if os.path.isdir(f) and re.match(r'^\d{4}-', f)]
folders.sort()

table_header = "| Problem | Topics | Solution |\n| :--- | :--- | :--- |\n"
table_rows = []

for folder in folders:
    num, name = format_name(folder)
    topics = TOPICS_MAP.get(num, "`-`")
    link = f"{REPO_URL}{folder}"
    table_rows.append(f"| **{num}. {name}** | {topics} | [View Code]({link}) |")

table_content = table_header + '\n'.join(table_rows)

with open(README_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = "\n## 🚀 LeetCode Progress\n\n"
end_tag = "\n\n"

new_content = re.sub(rf"(?s)({re.escape(start_tag)}).*?({re.escape(end_tag)})", rf"\1{table_content}\2", content)

with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)
