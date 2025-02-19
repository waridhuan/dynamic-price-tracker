from setuptools import setup, find_packages

setup(
    name="dynamic-price-tracker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'pandas',
        'numpy',
        'scikit-learn',
    ],
)