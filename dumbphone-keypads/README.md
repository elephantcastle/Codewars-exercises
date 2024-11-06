# Dumbphone Keypads

 - URL:[https://www.codewars.com/kata/5680e56f4797a55076000044](https://www.codewars.com/kata/5680e56f4797a55076000044)
 - Id: 5680e56f4797a55076000044
 - Language: python
 - Completed on: 2018-02-03T21:25:44.674Z
 - Tags: Fundamentals
 - Description:
Description:

Before smartphones and blackberry's without a qwerty keyboard, and prior to the development of T9 (predictive text entry) systems, the method to type words was called "multi-tap" and involved pressing a button repeatedly to cycle through the possible values.


    ------- ------- -------
    |     | | ABC | | DEF |
    |  1  | |  2  | |  3  |
    ------- ------- -------
    ------- ------- -------
    | GHI | | JKL | | MNO |
    |  4  | |  5  | |  6  |
    ------- ------- -------
    ------- ------- -------
    |PQRS | | TUV | | WXYZ|
    |  7  | |  8  | |  9  |
    ------- ------- -------
    ------- ------- -------
    |     | |space| |     |
    |  *  | |  0  | |  #  |
    ------- ------- -------

For example, to type a letter "R" you would press the 7 key three times (as the screen display for the current character cycles through P->Q->R->S->7). A character is "locked in" once the user presses a different key or pauses for a short period of time (thus, no extra button presses are required beyond what is needed for each letter individually). The zero key handles spaces, with one press of the key producing a space and two presses producing a zero.

For this assignment, write a module that can calculate the button presses sequence required for any phrase. Punctuation can be ignored for this exercise. Likewise, you can assume the phone doesn't distinguish between upper/lowercase characters (but you should allow your module to accept input in either for convenience).

For e.g. to type "HELLO WORLD", user would have to press the below sequence:
4433555p555666096667775553

p indicates a pause which is required before a character should get locked before the next character on the same key has to be pressed. In the above example, a pause is required before the keys can be pressed for the second instance of the character "L"

Try avoiding the obvious a-z combinations in order to support ease in change of Keypad combinations

