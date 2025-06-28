import shutil
from pathlib import Path

def convert_readme_to_index():
    root_dir = Path(__file__).resolve().parent.parent
    readme_path = root_dir / "README.md"
    index_path = root_dir / "src" / "docs" / "index.md"

    try:
        shutil.copyfile(readme_path, index_path)
        print(f"✅ تم تحويل {readme_path.name} إلى {index_path.relative_to(root_dir)} بنجاح.")
    except Exception as e:
        print(f"❌ حدث خطأ أثناء التحويل: {e}")

if __name__ == "__main__":
    convert_readme_to_index()
