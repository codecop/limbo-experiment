# tcr-in-practice

Try the TCR workflow on a larger code kata: [Snake](https://en.wikipedia.org/wiki/Snake_(video_game))

## Setup

To prepare the development environment:

```console
$ pip install -r requirements.txt
```

To install the package:

```console
$ pip install --editable .
```

## TCR

To run the TCR loop:

```console
$ ./tcr_loop   # for plain TCR
$ ./tcr+_loop  # for additional checks
```

For debugging purposes, consider running the bits and pieces
in `tcr` and `tcr+` in isolation.


## Play the Game

To play the game:

```console
$ snake
```


## Testing

### Inspect execution time

To display [test duration](https://docs.pytest.org/en/latest/how-to/usage.html#profiling-test-execution-duration):

```console
pytest --durations=0  # 0: display all instead of n-th slowest
```

### Selection

Two common options are:
1. Selecting on folder or file name, by either specifying a path or using the `-k` option
1. Selecting on a marker by using the `-m` option

For TCR we want our tests to run quickly an deselect those we do not need.
The `tkutil` tests include an example for a marker.

To use it:

```console
pytest -m "not tkutil"
```

Markers can also be [added at runtime](https://docs.pytest.org/en/6.2.x/example/markers.html#automatically-adding-markers-based-on-test-names).


However, as of now it seems easier to just select the relevant folder.

Hence:

```console
pytest tests/game
```
