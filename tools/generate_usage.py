# tools/generate_usage.py

import subprocess
import os
import sys

# تأكد من أن الإخراج يدعم UTF-8
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass  # متوافق مع الإصدارات القديمة

venv_python = os.path.join("venv_dev", "Scripts", "python.exe")

if not os.path.exists(venv_python):
    print("❌ لم يتم العثور على البيئة الافتراضية في venv_dev\\Scripts\\python.exe")
    sys.exit(1)

commands = [
    ("extract", ["extract", "--help"]),
    ("init", ["init", "--help"]),
    ("translate", ["translate", "--help"]),
    ("translate-all", ["translate-all", "--help"]),
    ("compile", ["compile", "--help"]),
    ("full", ["full", "--help"]),
]

output_lines = ["# 🧰 CLI Usage – jinja-i18n-tools\n"]

def clean_output(text):
    return (
        text.replace("→", "->")
            .replace("’", "'")
            .replace("“", '"')
            .replace("”", '"')
            .replace("\r\n", "\n")
    )

# إدراج help العام من ملف خارجي
try:
    with open("cli_help_output.txt", "r", encoding="utf-8") as f:
        help_output = f.read().strip()

    help_output = clean_output(help_output)
    output_lines.append("### `--help`\n```text\n" + help_output + "\n```\n")

except Exception as e:
    output_lines.append(f"⚠️ Failed to include --help: {e}\n")

# أوامر فرعية
for title, args in commands:
    output_lines.append(f"### `{title}`")

    try:
        result = subprocess.run(
            [venv_python, "-m", "jinja_i18n_tools", *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        output = result.stdout.strip() or result.stderr.strip()
        output = clean_output(output)
        output_lines.append(f"```text\n{output}\n```\n")

    except Exception as e:
        output_lines.append(f"⚠️ Failed to run `{title}`: {e}\n")

# حفظ النتيجة النهائية
try:
    with open("cli_usage.md", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
    print("✅ تم حفظ التوثيق الكامل في cli_usage.md")
except Exception as e:
    print(f"❌ فشل في حفظ الملف: {e}")
