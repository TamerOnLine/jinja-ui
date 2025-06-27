# file: utils.py or i18n_translations.py depending on your structure

import os
import shutil

def copy_babel_cfg_to_root():
    """
    Copy the babel.cfg file from the jinja_i18n_tools package to the external project's root.
    """
    # Absolute path to the current file's directory inside the package
    src_dir = os.path.dirname(__file__)
    src = os.path.join(src_dir, "babel.cfg")

    # Absolute path to the root of the external project using this package
    dst = os.path.join(os.getcwd(), "babel.cfg")

    # Copy the file only if it doesn't already exist in the root
    if not os.path.exists(dst):
        try:
            shutil.copy(src, dst)
            print(f"[📄] Copied babel.cfg to: {dst}")
        except Exception as e:
            print(f"[❌] Failed to copy babel.cfg: {e}")
    else:
        print("[ℹ️] babel.cfg already exists in the project root.")




def cleanup_babel_cfg_and_pot_file():
    """Remove messages.pot and babel.cfg from the project root after the process is complete."""
    pot_path = os.path.join(os.getcwd(), "messages.pot")
    if os.path.exists(pot_path):
        os.remove(pot_path)
        print("🧹 messages.pot has been deleted.")

    babel_path = os.path.join(os.getcwd(), "babel.cfg")
    if os.path.exists(babel_path):
        os.remove(babel_path)
        print("🧹 babel.cfg has been deleted from the project root.")


