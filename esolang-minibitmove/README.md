# Esolang: MiniBitMove

 - URL:[https://www.codewars.com/kata/587c0138110b20624e000253](https://www.codewars.com/kata/587c0138110b20624e000253)
 - Id: 587c0138110b20624e000253
 - Language: python
 - Completed on: 2022-06-13T13:23:41.059Z
 - Tags: Interpreters,Strings,Arrays,Bits,Esoteric Languages,Fundamentals
 - Description:
# Task:
This kata asks you to make a custom esolang interpreter for the language [MiniBitMove](https://esolangs.org/wiki/MiniBitMove). MiniBitMove has only two commands and operates on a array of bits. It works like this:

- `1`: Flip the bit at the current cell
- `0`: Move selector by 1

It takes two inputs, the program and the bits in needs to operate on. The program returns the modified bits. The program stops when selector reaches the end of the array. Otherwise the program repeats itself. **Note: This means that if a program does not have any zeros it is an infinite loop**

Example of a program that flips all bits in an array:
```
Code: 10
Bits: 11001001001010
Result: 00110110110101
```

After you're done, feel free to make translations and discuss this kata.
