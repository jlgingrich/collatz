# Collatz

A simple set of computational tools to test the [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture).

`collatz_lib.py` contains the function `run_collatz()` which, given an integer *n*, returns the *final value*, the *stopping time*, and the *maximum*. If the Collatz Conjecture is true, the *final value* should always be 1. Calling `run_collatz()` with `verbose=True` prints the values as they are calculated.

`collatz_shell.py` allows you to easily calculate the *stopping time* and *maximum* for any *n* using a command-line prompt.

`collatz_grapher.py` allows you to visualize how the *stopping time* and *maximum* change over a range of values using a command-line prompt. The figure will automatically be saved as an image file.
