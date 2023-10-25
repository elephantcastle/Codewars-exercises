# Linux history and  `!` command. Series#5  The `!?string` command

 - URL:[https://www.codewars.com/kata/581b29b549b2c0daeb001454](https://www.codewars.com/kata/581b29b549b2c0daeb001454)
 - Id: 581b29b549b2c0daeb001454
 - Language: python
 - Completed on: 2017-01-17T20:29:47.371Z
 - Tags: Strings,Parsers,Regular Expressions,Algorithms
 - Description:
All Unix user know the command line `history`. This one comes with a set of useful commands know as the `bang` command. 

For more information about the history command line you can take a look at: 

- The man page -> simply type `man history` in your terminal.
- The online man page [here](https://linux.die.net/man/3/history).
- And for more information about the `bang` command you can read [this article](http://jaysoo.ca/2009/09/16/unix-history-and-bang-commands/)

For this 5th kata we will explore the `!?string` command, according to the man page this one refer to the most recent command preceding the current postition in the history list containing string.

In this kata you should complete a function that take in an string that correspond to `s`, and an `history` with the following format: 

```
  1  cd /pub
  2  more beer
  3  lost
  4  ls 
  5  touch me 
  6  chmod 000 me 
  7  more me
  8  history
```

and that should return the most recent command line that contains executed command line `s`, for example with `s`="me" and the above history it should return `more me`. If user ask for a `s` without any know entry for example `n=you` here, the function should return `!you: event not found`.

**Note**: Lot of the command line comes form some geeky t-shirt and form this [excellent page](http://langevin.univ-tln.fr/cours/UPS/extra/unix-shell-jokes.txt).



