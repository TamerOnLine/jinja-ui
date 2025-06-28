import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# تحميل البيانات من project_config.json
config_path = Path("project_config.json")
with config_path.open(encoding="utf-8") as f:
    config = json.load(f)

# إعداد Jinja2
env = Environment(loader=FileSystemLoader("tools/templates"))
template = env.get_template("about_template.md.j2")

# توليد الناتج
output = template.render(**config)

# كتابة الملف النهائي
destination = Path("src/docs/about.md")
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(output, encoding="utf-8")

print("✅ src/docs/about.md تم إنشاؤه بنجاح.")
