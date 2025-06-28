# CLI Usage

This section describes how to use the command-line interface (CLI).

## `jinja-i18n-tools --help`

⚠️ Failed to generate help for `jinja-i18n-tools --help`

```bash
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "T:\jinja-ui\venv\Lib\site-packages\jinja_i18n_tools\__main__.py", line 4, in <module>
    main()
  File "T:\jinja-ui\venv\Lib\site-packages\jinja_i18n_tools\cli.py", line 46, in main
    args = parser.parse_args()
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\argparse.py", line 1904, in parse_args
    args, argv = self.parse_known_args(args, namespace)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\argparse.py", line 1914, in parse_known_args
    return self._parse_known_args2(args, namespace, intermixed=False)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\argparse.py", line 1943, in _parse_known_args2
    namespace, args = self._parse_known_args(args, namespace, intermixed)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\argparse.py", line 2184, in _parse_known_args
    start_index = consume_optional(start_index)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\argparse.py", line 2113, in consume_optional
    take_action(action, args, option_string)
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\argparse.py", line 2018, in take_action
    action(self, namespace, argument_values, option_string)
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\argparse.py", line 1148, in __call__
    parser.print_help()
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\argparse.py", line 2621, in print_help
    self._print_message(self.format_help(), file)
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\argparse.py", line 2627, in _print_message
    file.write(message)
  File "C:\Users\Tamer\AppData\Local\Programs\Python\Python312\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\u2192' in position 511: character maps to <undefined>
```

## `jinja-i18n-tools extract --help`

```bash
usage: __main__.py extract [-h]

options:
  -h, --help  show this help message and exit
```

## `jinja-i18n-tools compile --help`

```bash
usage: __main__.py compile [-h]

options:
  -h, --help  show this help message and exit
```

## `jinja-i18n-tools translate --help`

```bash
usage: __main__.py translate [-h] --lang LANG [--force]

options:
  -h, --help   show this help message and exit
  --lang LANG
  --force
```

## `jinja-i18n-tools translate-all --help`

```bash
usage: __main__.py translate-all [-h]

options:
  -h, --help  show this help message and exit
```

## `jinja-i18n-tools init --help`

```bash
usage: __main__.py init [-h]

options:
  -h, --help  show this help message and exit
```

## `jinja-i18n-tools full --help`

```bash
usage: __main__.py full [-h] [--lang LANG] [--force]

options:
  -h, --help   show this help message and exit
  --lang LANG  Language to translate (or 'all')
  --force
```

