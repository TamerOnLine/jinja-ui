# 🧩 jinja-i18n-tools

Automated i18n tool for Jinja2-based projects using Babel and Google Translate.

## 📦 Features

- 🔍 Extract translatable strings from your Jinja2 templates.
- 🌐 Initialize `.po` files for multiple languages.
- 🤖 Auto-translate using Google Translate via `deep_translator`.
- 🛠️ Compile `.po` files into `.mo`.
- 🧹 Automatically cleans up temporary files like `messages.pot` and `babel.cfg`.

---

## ⚙️ Installation

```bash
pip install jinja-i18n-tools
```

---

## 🚀 Usage

Activate your virtual environment, then run:

```bash
jinja-i18n full
```

This will:
1. Copy `babel.cfg` to your project root.
2. Extract translatable strings from your templates.
3. Initialize translation files for each language.
4. Auto-translate all strings.
5. Compile `.po` files into `.mo`.
6. Clean up temporary files.

---

## 🛠️ CLI Commands

```bash
jinja-i18n extract
jinja-i18n init
jinja-i18n translate --lang ar
jinja-i18n translate-all
jinja-i18n compile
jinja-i18n full --lang all --force
```

---

## 🌍 Languages

By default, the following languages are supported:

- `ar` – Arabic
- `de` – German

You can customize this in the source by editing the `LANGUAGES` list.

---

## 📁 Project Structure

Your Jinja2 templates and Python files must be located where your `babel.cfg` expects them. Here's a recommended configuration:

```
[python: **.py]
[jinja2: templates/**.html]
[jinja2: templates/**.j2] 
extensions=jinja2.ext.i18n
```

This configuration instructs `pybabel` to:

- Extract translation strings from **all Python files** recursively.
- Extract translatable content from **all `.html` templates** under the `templates/` folder.
- Enable the `jinja2.ext.i18n` extension to support `{% trans %}` blocks.

Make sure this file (`babel.cfg`) is located in your project root **temporarily**, or is copied automatically by the tool before running `pybabel extract`.

---

## 🧼 Cleanup

Temporary files like `babel.cfg` and `messages.pot` are deleted automatically after the process finishes.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it with attribution.  
Feel free to explore and build upon it!

---

## 👨‍💻 About the Author

🎯 **Tamer OnLine – Developer & Architect**  
A dedicated software engineer and educator with a focus on building multilingual, modular, and open-source applications using Python, Flask, and PostgreSQL.

🔹 Founder of **Flask University** – an initiative to create real-world, open-source Flask projects  
🔹 Creator of [@TamerOnPi](https://www.youtube.com/@mystrotamer) – a YouTube channel sharing tech, tutorials, and Pi Network insights  
🔹 Passionate about helping developers learn by building, one milestone at a time

Connect or contribute:

[![GitHub](https://img.shields.io/badge/GitHub-TamerOnLine-181717?style=flat&logo=github)](https://github.com/TamerOnLine)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/tameronline/)  
[![YouTube](https://img.shields.io/badge/YouTube-TamerOnPi-red?style=flat&logo=youtube)](https://www.youtube.com/@mystrotamer)

---
> 💡 **Got feedback or want to collaborate?**  
> Open an issue, fork the repo, or just say hi on LinkedIn!
