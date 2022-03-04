"""
Check size of change set.

Allows to limit the acceptable size of a change in a single loop.
If not set, defaults to infinity.
"""
import sys
import subprocess

import click


@click.command()
@click.option("--added", default=float("inf"), help="Maximum number of added lines")
def cli_is_change_size_okay(added):
    git_diff_numstat = get_git_diff_numstat()
    sys.exit(int(not is_change_size_okay(git_diff_numstat, added)))


def is_change_size_okay(git_diff_numstat, added):
    total_added, total_removed = compute_lines_changed(git_diff_numstat)
    return total_added - total_removed <= added


def get_git_diff_numstat():
    cmd = "git diff --numstat"
    result = subprocess.run(cmd, shell=True, check=True, capture_output=True)
    msg = result.stdout.decode()
    return msg


def compute_lines_changed(git_diff_numstat):
    total_added, total_removed = 0, 0
    for line in git_diff_numstat.splitlines():
        added, removed, _ = line.split("\t")
        total_added += int(added)
        total_removed += int(removed)
    return (total_added, total_removed)


if __name__ == "__main__":
    cli_is_change_size_okay()
