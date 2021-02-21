# to_tty

This is a program to redirect output to other TTYs in linux environments.

## Example Usage

### Save a tty

```bash
$ to_tty -s my_tty # save the current terminal as the output under the name 'my-tty'
```

### Send text to that TTY

in another terminal:
```bash
$ echo 'abc' | to_tty my_tty
```
`abc` appears in the first terminal

### Run a command like its in the first terminal
This works by reading the environment variables from the first terminal and setting the environment for the command passed to `to_tty`.
```bash
$ to_tty my_tty -c 'echo $COLUMNS'
```
will output the width of the first (display) terminal, and not the second (driver).
This behaviour differs from `echo $COLUMNS | to_tty my_tty`, which will output the width of the second (driver) terminal.

This is useful if you want to run programs that output text formatted to the size of the terminal.

## Installation
TODO
