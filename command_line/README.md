# Command Line Scripting 

## `samples` Directory
This is a collection of sample text files, intended for practice with filesystem tricks (see below).

## `simple` Directory
This consists of very simple bash scripts, which demonstrate basic functions. `cd` into the simple directory and run the following:

`sh create_file.sh` -- simply creates, then copies a text file to a hardcoded filename
`sh create_custom_file.sh myfile.txt` -- similar to above, but allows passing a custom filename as an 'argument' (in this case, 'myfile.txt')


## `processor` Directory
This directory demostrates how a few different bash scripts can be joined together to create a more complex set of actions, while still keeping the individual operations clear and discrete.

- `1_A_BGD_3_F_11127.txt` - A text file with text to be processed
- `cleanup.sh` - Script to delete the output directory
- `copy.sh` - Copy file, passed as an argument, to output directory
- `deidentify.sh` - Find-replace proper names
- `tag.sh` - Prepend filename within file in output directory
- `main.sh` - Wrapper script that executes `copy.sh`, `deidentify.sh`, and `tag.sh`

### Example usage
Run `sh main.sh 1_A_BGD_3_F_11127.txt`.

An `output` directory will be created, with a new file called `1_A_BGD_3_F_11127.txt`. The text will undergo the following change:

Before:
> Then he remembered that the Reggie Chiverses, whose house was a few doors above, were taking a large party that evening to see Adelaide Neilson in Romeo and Juliet,

After:

> <Filename : 1_A_BGD_3_F_11127.txt>
Then he remembered that the `<NAME>` `<NAME>`es, whose house was a few doors above, were taking a large party that evening to see Adelaide Neilson in Romeo and Juliet,

Running `cleanup.sh` will remove the output directory.

## Bash Filesystem manipulation tricks

Below are snippets of different filesystem inspection/searching tricks that are useful to know.

Each command is designed to be run against the files present in the `samples` directory. To run any of these commands and see the output first enter that directory (`cd samples`), then run the command as shown.

First off, know the "pipe" separator: `|`. This is a fundamental way to send (pipe) the output of one command to another command. You'll see it a lot, below.

## cat
`cat` (short for "concatenate") is a multipurpose command which, at its simplest, prints the contents of a file and can write output to files. A nice overview of some simple `cat` commands is at https://www.tecmint.com/13-basic-cat-command-examples-in-linux/

Try running the following:

`cat 0.txt`
`cat 0.txt 1.txt 2.txt`
`cat 0.txt 1.txt 2.txt | more`

## grep
`grep` (global regular expression print) is a very powerful, multipurpose command, but for simplicity, you can think of it as a search command.

`grep "Why" 3.txt` - search the file 3.txt for the word "Why"
`grep -r "Why" .` - search all files for the word "Why"
`grep -ir "Why" *.txt` - search all .txt files, case-insensitive, for "why"
`grep -ir " *navigated " *.txt` -- find texts that include a word that ends with -navigated.

## find
`find` is a way to search within filenames specifically.

### Unix-like systems (Mac)
`cd ..`
`find . -name *.txt` -- will find all files in the current directory of type `.txt`

### Windows
`Get-ChildItem -Filter *.txt -Recurse`

## sort
`sort`, as its name implies, sorts things alphabetically or numerically. This can be used to sort lines in a single file, or sort the output of other commands you run on multiple files. The next example will first get the output of the directory (via the `ls` command), and then "pipe" that output (`|`) to the `sort` command, and sort by the 5th column (which *should* be the filesize):

`ls -al | sort -k5` (Will only work on Unix-like systems)

`sort 7.txt` will sort all of the lines in `7.txt` alphabetically

`sort 7.txt | uniq -c` will print all lines that are *unique*, followed by the instances of the line.

`sort 7.txt | uniq -c | sort -nr` will subsequently display those lines, ordered by count, descending.

Here's a good resource on the `sort` command: https://www.skorks.com/2010/05/sort-files-like-a-master-with-the-linux-sort-command-bash/