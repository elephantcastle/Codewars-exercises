# Pawn Promotion

 - URL:[https://www.codewars.com/kata/62652939385ccf0030cb537a](https://www.codewars.com/kata/62652939385ccf0030cb537a)
 - Id: 62652939385ccf0030cb537a
 - Language: python
 - Completed on: 2022-06-27T20:58:46.481Z
 - Tags: Fundamentals
 - Description:
# Welcome To Pawn Promotion Kata.


In this kata you will write a program that studies a chess board
that contains only two pieces (pawn) and (king).

The pawn is always in the last row
as it will now turn into one of the four pieces
```[queen , bishop , knight , rook ]``` in a process called {pawn promotion}.

Your task is to locate the king and the pawn and choose the appropriate piece
to promote it and put the king in check.

```The letter P represents the pawn```

```The letter K represents the king```

# Examples:
```
input:
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['P', ' ', ' ', 'K', ' ', ' ', ' ', ' '],

output:
['queen', 'rook']
```
```
input:
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', 'K', ' '],
[' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],

output:
['knight']
```

```
input:
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', 'K', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', 'P', ' ', ' ', ' ', ' ', ' '],

output:
[]
```

# Q&A:
```
Q:- Why was the order of the pieces in the first example as ['queen', 'rook']
and not the other way around ?
```
```
A:- In the event that there is more than one option that achieves check,
return the order of the pieces as follows [queen, bishop, knight, rook]
```

# special cases:

- If there is no piece that can make check immediately upon upgrade, return [].

- If there is no pawn on the board, return [].

- If there is no king on the board, return [].
