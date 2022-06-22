from setuptools import setup, find_packages

setup(
    name="tcr-snake-limbo",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "check_coverage = tcr.check_coverage:cli",
            "check_change = tcr.check_change:cli",
            "snake = game.main:run",
        ]
    },
)
