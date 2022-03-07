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
def cli(old, new):
    old = from_json(old)
    new = from_json(new)
    sys.exit(int(not is_coverage_geq_than_before(old, new)))


def is_coverage_geq_than_before(old, new):
    return get_coverage_metric(old) >= get_coverage_metric(new)


def from_json(path):
    with open(path, "r") as fh:
        data = json.load(fh)
    return data


def get_coverage_metric(data):
    return data["totals"]["missing_lines"]
