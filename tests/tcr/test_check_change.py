from tcr.check_change import compute_lines_changed


def test_compute_number_of_lines_changed():
    output = "3\t0\tcheck_coverage.py\n3\t2\tconftest.py\n"
    expected = (6, 2)

    assert compute_lines_changed(output) == expected
