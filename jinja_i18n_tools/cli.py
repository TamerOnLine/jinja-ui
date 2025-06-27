# cli.py
import os
import argparse
from . import i18n_auto, i18n_compile, i18n_translations, utils



def translate(lang, force=False):
    """Translate .po files for a specific language or all languages."""
    if lang == "all":
        from .i18n_translations import LANGUAGES
        for l in LANGUAGES:
            print(f"[🌐] Translating to {l}")
            i18n_auto.auto_translate_po_files_by_lang(l, force=force)
    else:
        print(f"[🌐] Translating to {lang}")
        i18n_auto.auto_translate_po_files_by_lang(lang, force=force)

def main():
    parser = argparse.ArgumentParser(description="Jinja i18n Tools CLI")
    subparsers = parser.add_subparsers(dest="command")

    # extract
    subparsers.add_parser("extract", help="Extract translatable strings.")

    # init
    subparsers.add_parser("init", help="Initialize languages.")

    # translate
    parser_translate = subparsers.add_parser("translate", help="Translate to specific language.")
    parser_translate.add_argument("--lang", required=True)
    parser_translate.add_argument("--force", action="store_true")

    # translate-all
    subparsers.add_parser("translate-all", help="Translate all languages.")

    # compile
    subparsers.add_parser("compile", help="Compile translations.")

    # full process (lang is now optional with default="all")
    parser_full = subparsers.add_parser("full", help="Run full process (extract → init → translate → compile)")
    parser_full.add_argument("--lang", default="all", help="Language to translate (or 'all')")
    parser_full.add_argument("--force", action="store_true")

    # Parse arguments
    args = parser.parse_args()

    if args.command == "extract":
        i18n_translations.extract_messages()

    elif args.command == "init":
        i18n_translations.init_languages()

    elif args.command == "translate":
        translate(args.lang, force=args.force)

    elif args.command == "translate-all":
        translate("all")

    elif args.command == "compile":
        i18n_compile.compile_translations()

    elif args.command == "full":
        print("[🔁] Running full process...")
        utils.copy_babel_cfg_to_root()
        i18n_translations.extract_messages()
        i18n_translations.init_languages()
        translate(args.lang, force=args.force)
        i18n_compile.compile_translations()
        utils.cleanup_babel_cfg_and_pot_file()


        print("[✅] All done!")

    else:
        parser.print_help()
