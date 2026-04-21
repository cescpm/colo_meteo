from setuptools import setup, find_packages

setup(
    name         ="colo_meteo",
    version      ="1.0.0",
    author       ="Parera",
    author_email ="cescparera12@gmail.com",
    description  ="A library for accessing Colombian WS data from IDEAM",
    long_description = open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = "text/markdown",
    url          = "https://github.com/cescpm/colo_meteo",
    packages     = find_packages(where="."),

    python_requires  = ">=3.8",
    install_requires = [
        "sodapy >= 2.2.0",
        "pandas >= 3.0.1"
    ],
    project_urls     = {
        "Bug Reports" : "https://github.com/cescpm/colo_meteo/issues",
        "Source"      : "https://github.com/cescpm/colo_meteo",
    },
)
