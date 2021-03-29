from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="create_python_app",
    version="0.1.0",
    description="CLI tool to quickstart Python app.",
    license="MIT",
    author="averak",
    packages=find_packages(),
    package_data={'create_python_app': ['template']},
    install_requires=["jinja2"],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        'console_scripts': [
            'create-python-app=create_python_app.core:main',
        ]
    },
)
