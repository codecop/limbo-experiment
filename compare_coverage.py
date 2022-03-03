"""
Compare coverage results between runs.

Coverage can create a JSON report which, amongst other details, 
includes the total percent covered.
This quantity is comparted for the two reports passed.
"""
import json
import sys

import click


@click.command()
@click.argument("old", type=click.Path(exists=True))
@click.argument("new", type=click.Path(exists=True))
def cli_is_coverage_geq_than_before(old, new):
    if is_coverage_geq_than_before(old, new):
        sys.exit(0)
    sys.exit(1)


def is_coverage_geq_than_before(old, new):
    return get_percent_covered_from_json(old) <= get_percent_covered_from_json(new)


def get_percent_covered_from_json(file):
    return get_percent_covered(from_json(file))


def from_json(path):
    with open(path, "r") as fh:
        data = json.load(fh)
    return data


def get_percent_covered(data):
    return data["totals"]["percent_covered"]


if __name__ == "__main__":
    cli_is_coverage_geq_than_before()
