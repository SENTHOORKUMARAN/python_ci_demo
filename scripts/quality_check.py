import ast
import pathlib
import sys

MAX_LINES = 100

errors = []

for pyfile in pathlib.Path(".").rglob("*.py"):
    if "__pycache__" in str(pyfile):
        continue

    with open(pyfile, "r") as f:
        lines = f.readlines()

    if len(lines) > MAX_LINES:
        errors.append(
            f"{pyfile}: exceeds {MAX_LINES} lines ({len(lines)})"
        )

    try:
        tree = ast.parse("".join(lines))
    except Exception as e:
        errors.append(f"{pyfile}: parse error {e}")
        continue

    for node in ast.walk(tree):
        if isinstance(
            node,
            (ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            if ast.get_docstring(node) is None:
                errors.append(
                    f"{pyfile}: function '{node.name}' missing docstring"
                )

if errors:
    print("QUALITY CHECK FAILED")
    for err in errors:
        print(err)
    sys.exit(1)

print("QUALITY CHECK PASSED")
