from setuptools import setup, find_packages

# تحميل المتطلبات تلقائيًا من requirements.txt
def load_requirements(path="requirements.txt"):
    with open(path) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="project_story",
    version="0.1.0",
    description="A CLI tool for managing and narrating project workflows",
    author="Tamer",
    author_email="info@denkengewinnen.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=load_requirements(),  # تحميل تلقائي للمكتبات
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "project-story=project_story.cli:main"
        ]
    },
)
