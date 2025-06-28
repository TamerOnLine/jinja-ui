from pathlib import Path

source = Path("LICENSE")
destination = Path("src/docs/license.md")

# تأكد من وجود المجلد
destination.parent.mkdir(parents=True, exist_ok=True)

if source.exists():
    content = source.read_text()
    destination.write_text(f"# 📄 License\n\n```\n{content}\n```", encoding="utf-8")
    print("✅ src/docs/license.md تم إنشاؤه بنجاح.")
else:
    print("❌ ملف LICENSE غير موجود.")
