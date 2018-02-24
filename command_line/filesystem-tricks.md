# Bash Filesystem manipulation tricks

This file contains lists different filesystem inspection/searching tricks that are useful to know.

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