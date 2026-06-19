import json
import os
import subprocess

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

changed_files = run("git diff --name-only origin/master...HEAD").splitlines()

files_changed = len(changed_files)

stat = run("git diff --shortstat origin/master...HEAD")

todos = []

for f in changed_files:
    try:
        with open(f, "r", errors="ignore") as fp:
            for i, line in enumerate(fp, 1):
                if "TODO" in line or "FIXME" in line:
                    todos.append(f"{f}:{i}: {line.strip()}")
    except:
        pass

diff_stat = run("git diff --stat origin/master...HEAD")

report = f"""## Automated PR Review

### Summary
- Files changed: {files_changed}
- Diff summary: {stat}

### TODO / FIXME

"""

if todos:
    report += "\n".join(f"- {x}" for x in todos)
else:
    report += "No TODO/FIXME found."

report += f"\n\n### Diff Statistics\n```\n{diff_stat}\n```"

with open("review_comment.md", "w") as f:
    f.write(report)

print(report)
