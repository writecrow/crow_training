# Command Line Scripting Demo

This repository demostrates how a few different bash scripts can be joined together to create a more complex set of actions, while still keeping the individual operations clear and discrete.

- `1_A_BGD_3_F_11127.txt` - A text file with text to be processed
- `cleanup.sh` - Script to delete the output directory
- `copy.sh` - Copy file, passed as an argument, to output directory
- `deidentify.sh` - Find-replace proper names
- `tag.sh` - Prepend filename within file in output directory
- `main.sh` - Wrapper script that executes `copy.sh`, `deidentify.sh`, and `tag.sh`

## Example usage
Run `sh main.sh 1_A_BGD_3_F_11127.txt`.

An `output` directory will be created, with a new file called `1_A_BGD_3_F_11127.txt`. The text will undergo the following change:

Before:
> Then he remembered that the Reggie Chiverses, whose house was a few doors above, were taking a large party that evening to see Adelaide Neilson in Romeo and Juliet,

After:

> <Filename : 1_A_BGD_3_F_11127.txt>
Then he remembered that the `<NAME>` `<NAME>`es, whose house was a few doors above, were taking a large party that evening to see Adelaide Neilson in Romeo and Juliet,

Running `cleanup.sh` will remove the output directory.