# to_tty

This is a program to redirect output to other terminals in linux environments.

## Example Usage

### Save a tty

```bash
$ to-tty -s my_tty # save the current terminal as the output under the name 'my-tty'
```

### Send text to that TTY

in another terminal:
```bash
$ echo 'abc' | to-tty my_tty
```
`abc` appears in the first terminal

### Run a command and fit it to the first terminal
This works by reading the row/colmun environment variables from the first terminal and setting the environment for the command passed to `to-tty`.

```bash
$ to-tty my_tty -c 'echo $COLUMNS'
```
will output the width of the first (display) terminal, and not the second (driver).
This behaviour differs from `echo $COLUMNS | to-tty my_tty`, which will output the width of the second (driver) terminal.

This is useful if you want to run programs that output text formatted to the size of the terminal.

The other thing this is useful for is getting color back for some outputs. For example:
```bash
$ python -c 'junk' 2>&1 | to-tty my_tty
```
will print the error, but without color.
```bash
$ to-tty my_tty -c "python -c 'junk'"
```
will include color in the output terminal.

## Installation
TODO
