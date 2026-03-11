from setuptools import setup, find_packages

setup(
    name="meupia-grid",
    version="1.0.2",
    description="Plugin oficial do ecossistema meuPiá para visualização de Grids 2D (A*, BFS, DFS).",
    author="Henry Hamon",
    author_email="henryhamon@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)