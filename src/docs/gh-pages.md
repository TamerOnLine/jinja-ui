# 🌐 GitHub Pages Deployment Guide

This guide explains how to deploy documentation using **MkDocs** and publish it via **GitHub Pages** (`gh-pages` branch).

---

## 📘 What is `gh-pages`?

`gh-pages` is a special branch on GitHub used to host static websites directly from your repository.
You can use it to publish documentation, blogs, or project pages without any external server.

---

## ⚙️ Requirements

- A GitHub repository.
- A documentation folder (e.g., `docs/` or `src/docs/`).
- A `mkdocs.yml` configuration file.
- GitHub Pages enabled from repository settings.

---

## 🔧 Setup Steps

### 1️⃣ Create `mkdocs.yml`

```yaml
site_name: Your Project Docs
docs_dir: src/docs
theme:
  name: material
```

### 2️⃣ Create `gh-pages-requirements.txt` (optional)

```
mkdocs
mkdocs-material
```

### 3️⃣ Setup GitHub Actions

Create a file at `.github/workflows/docs.yml`:

```yaml
name: 📘 Build and Deploy MkDocs

on:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: 🔁 Checkout repository
        uses: actions/checkout@v3

      - name: 🐍 Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: 📦 Install dependencies
        run: |
          pip install -r gh-pages-requirements.txt

      - name: 🚀 Deploy MkDocs to GitHub Pages
        env:
          GIT_COMMITTER_NAME: github-actions[bot]
          GIT_COMMITTER_EMAIL: github-actions[bot]@users.noreply.github.com
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          git config --global user.name "$GIT_COMMITTER_NAME"
          git config --global user.email "$GIT_COMMITTER_EMAIL"
          mkdocs gh-deploy --force
```

---

### 4️⃣ Enable GitHub Pages

Go to:  
**Settings → Pages → Source → Deploy from a branch → `gh-pages` + root folder**, then click **Save**.

---

### 🌍 Your documentation will be live at:

```
https://<username>.github.io/<repository-name>/
```

Example:
```
https://tameronline.github.io/jinja-ui/
```

---

## 🧠 Notes

- Every push to `main` triggers an update.
- Do **not** manually edit the `gh-pages` branch.
- You can enhance `mkdocs.yml` with logo, nav, colors, plugins, and more.

---

## 🔗 Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages Guide](https://docs.github.com/en/pages)