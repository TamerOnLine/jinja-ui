import os
import subprocess

def compile_translations(translations_dir='translations'):
    for root, dirs, files in os.walk(translations_dir):
        for file in files:
            if file.endswith('.po'):
                po_path = os.path.join(root, file)
                cmd = f"pybabel compile -i \"{po_path}\" -o \"{po_path[:-3]}.mo\""
                print(f"Compiling {po_path} ...")
                subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    compile_translations()
    print("All .po files compiled to .mo files.")
