from setuptools import setup, find_packages

setup(
    name="jinja_i18n_tools",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,  
    package_data={
        "jinja_i18n_tools": ["babel.cfg"],
    },
    install_requires=[
        "polib",
        "deep-translator",
    ],
    entry_points={
        'console_scripts': [
            'jinja-i18n = jinja_i18n_tools.cli:main',
        ],
    },
)
