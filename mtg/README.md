### Table of content

0. [Mark Down Table](#mark-down-table)

1. [How to use](#how-to-use)

2. [Specify the level of Heading included](#specify-the-level-of-heading-included)

3. [Tips & Advice](#tips-&-advice)

4. [The program is made in python](#the-program-is-made-in-python)

5. [it work from the terminal](#it-work-from-the-terminal)

6. [the end](#the-end)

# Mark Down Table
Mark Down Table or Mdtable is a python program that will add a table of content at the beginning of your mark down file.

# How to use
```
python3 mdtable.py fileName.md 
```

## Specify the level of Heading included
```
python3 mdtable.py fileName.md h1 h3
```
> This example will include only the Heading of level one and three to the table of contents. 
> If No header is specified it will only included h1 by default.
> If another header then h1 is specified then h1 will not be included by default.

### Tips & Advice
This program only work with the default syntax and only consider headers level 1 to 6 marked with the symbol __#__ alternative syntax wont work.

