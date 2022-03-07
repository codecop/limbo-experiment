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
