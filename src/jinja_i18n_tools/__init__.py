import os
from .i18n_translations import extract_messages, init_languages, cleanup_pot_file,  POT_FILE
from .i18n_auto import auto_translate_po_files_by_lang
from .i18n_compile import compile_translations
from .utils import cleanup_babel_cfg_and_pot_file, copy_babel_cfg_to_root


def run_all(lang="ar", force=False):
    print("[🔁] Running full process...")
    copy_babel_cfg_to_root()
    extract_messages()
    init_languages()
    auto_translate_po_files_by_lang(lang, force=force)
    compile_translations()
    cleanup_pot_file()
    cleanup_babel_cfg_and_pot_file()

    print("[✅] All done!")
