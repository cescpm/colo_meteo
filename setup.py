from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="colo_meteo",
    version="1.0.0",
    author="Parera",
    author_email="cescparera12@gmail.com",
    description="A library for accessing Colombian WS data from IDEAM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cescpm/colo_meteo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ],
    python_requires=">=3.8",
    install_requires=[
        "sodapy>=2.2.0",
        "pandas>=3.0.1"
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    keywords="colombia weather ideam meteorological data climate",
    project_urls={
        "Bug Reports": "https://github.com/cescpm/colo_meteo/issues",
        "Source": "https://github.com/cescpm/colo_meteo",
    },
)
