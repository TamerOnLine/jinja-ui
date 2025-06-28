import subprocess
import os

venv_python = os.path.join("venv", "Scripts", "python.exe")

print("📦 Capturing --help safely...")

result = subprocess.run(
    [venv_python, "-m", "jinja_i18n_tools", "--help"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    encoding="utf-8",
    errors="replace",
    env={**os.environ, "PYTHONIOENCODING": "utf-8"},
)

# دمج stdout و stderr
output = result.stdout + "\n" + result.stderr

# استبدال الرموز التي تسبب UnicodeError عند القراءة
output = output.replace("→", "->")

# الحفظ
with open("cli_help_output.txt", "w", encoding="utf-8") as f:
    f.write(output.strip())

print("✅ Saved --help output to cli_help_output.txt")
