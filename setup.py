from lyncs_setuptools import setup

requirements = [
    "dill",
    "dataclasses",
    "varname",
    "tabulate",
    "numpy",
    "lyncs_utils",
]

extras = {
    "graph": [
        "graphviz",
    ],
    "test": ["pytest", "pytest-cov"],
    "optuna": ["optuna"],
}

setup(
    "tuneit",
    install_requires=requirements,
    extras_require=extras,
)
