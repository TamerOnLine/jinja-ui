import os
import polib
from deep_translator import GoogleTranslator

def auto_translate_po(file_path, dest_lang='ar', force=False):
    po = polib.pofile(file_path)
    
    entries = po if force else [entry for entry in po if not entry.translated()]
    print(f"Found {len(entries)} {'entries' if force else 'untranslated entries'} in {file_path}.")

    for entry in entries:
        try:
            translated_text = GoogleTranslator(source='auto', target=dest_lang).translate(entry.msgid)
            entry.msgstr = translated_text
            print(f'Translated "{entry.msgid}" to "{entry.msgstr}"')
        except Exception as e:
            print(f"Error translating '{entry.msgid}': {e}")

    po.save(file_path)
    print(f"Translations saved to {file_path}")

def translate_all_po_files(translations_dir='translations'):
    for root, dirs, files in os.walk(translations_dir):
        for file in files:
            if file.endswith('.po'):
                po_path = os.path.join(root, file)
                parts = po_path.split(os.sep)
                try:
                    lang = parts[parts.index('translations') + 1]
                except (ValueError, IndexError):
                    lang = 'en'
                print(f"Translating file {po_path} to language '{lang}'")
                auto_translate_po(po_path, dest_lang=lang)

def auto_translate_po_files_by_lang(lang, translations_dir='translations', force=False):
    for root, dirs, files in os.walk(translations_dir):
        for file in files:
            if file.endswith('.po') and f"/{lang}/" in os.path.join(root, file).replace("\\", "/"):
                po_path = os.path.join(root, file)
                auto_translate_po(po_path, dest_lang=lang, force=force)

if __name__ == "__main__":
    translate_all_po_files()
