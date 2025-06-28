import os
import subprocess

PROJECT_DIR = os.path.abspath('.')  
LOCALES_DIR = os.path.join(PROJECT_DIR, 'translations')
POT_FILE = os.path.join(PROJECT_DIR, 'messages.pot')
BABEL_CFG = os.path.join(PROJECT_DIR, 'babel.cfg')
LANGUAGES = ['ar', 'de']  

def run_cmd(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error:\n{result.stderr}")
    else:
        print(result.stdout)

def extract_messages():
    cmd = f"pybabel extract -F {BABEL_CFG} -o {POT_FILE} {PROJECT_DIR}"
    run_cmd(cmd)

def init_languages():
    for lang in LANGUAGES:
        lang_po_file = os.path.join(LOCALES_DIR, lang, "LC_MESSAGES", "messages.po")
        if not os.path.exists(lang_po_file):
            print(f"Initializing language: {lang}")
            cmd = f"pybabel init -i {POT_FILE} -d {LOCALES_DIR} -l {lang}"
            run_cmd(cmd)
        else:
            print(f"Language {lang} already initialized.")

def compile_translations():
    cmd = f"pybabel compile -d {LOCALES_DIR}"
    run_cmd(cmd)

def cleanup_pot_file():
    if os.path.exists(POT_FILE):
        os.remove(POT_FILE)
        print("messages.pot has been deleted.")

if __name__ == "__main__":
    extract_messages()
    init_languages()
    compile_translations()
    cleanup_pot_file()
    print("✅ Done! You can now edit the .po files in translations/<lang>/LC_MESSAGES/messages.po")
