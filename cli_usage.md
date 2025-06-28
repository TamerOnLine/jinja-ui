# 🧰 CLI Usage – jinja-i18n-tools

### `--help`
```text
usage: __main__.py [-h]
                   {extract,init,translate,translate-all,compile,full} ...

Jinja i18n Tools CLI

positional arguments:
  {extract,init,translate,translate-all,compile,full}
    extract             Extract translatable strings.
    init                Initialize languages.
    translate           Translate to specific language.
    translate-all       Translate all languages.
    compile             Compile translations.
    full                Run full process (extract -> init -> translate ->
                        compile)

options:
  -h, --help            show this help message and exit
```

### `extract`
```text
usage: __main__.py extract [-h]

options:
  -h, --help  show this help message and exit
```

### `init`
```text
usage: __main__.py init [-h]

options:
  -h, --help  show this help message and exit
```

### `translate`
```text
usage: __main__.py translate [-h] --lang LANG [--force]

options:
  -h, --help   show this help message and exit
  --lang LANG
  --force
```

### `translate-all`
```text
usage: __main__.py translate-all [-h]

options:
  -h, --help  show this help message and exit
```

### `compile`
```text
usage: __main__.py compile [-h]

options:
  -h, --help  show this help message and exit
```

### `full`
```text
usage: __main__.py full [-h] [--lang LANG] [--force]

options:
  -h, --help   show this help message and exit
  --lang LANG  Language to translate (or 'all')
  --force
```
