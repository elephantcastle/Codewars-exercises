# T.T.T.27: Four piles of apples

 - URL:[https://www.codewars.com/kata/57aae4facf1fa57b3300005d](https://www.codewars.com/kata/57aae4facf1fa57b3300005d)
 - Id: 57aae4facf1fa57b3300005d
 - Language: python
 - Completed on: 2017-07-15T14:05:52.290Z
 - Tags: Puzzles,Games
 - Description:
## Problem

There are `n` apples that need to be divided into four piles. We need two mysterious number `x` and `y`. Let The number of first pile equals to `x+y`, the number of second pile equals to `x-y`, the number of third pile equals to `x*y`, the number of fourth pile equals to `x/y`. We need to calculate how many apples are there in each pile.

Of course, there won't be so many unknowns. We know the total number of apples(`n`) and the second mysterious number(`y`). 

For example: there are 48 apples need to divided into four piles. y=3. that is, 1st pile should be x+3, 2nd pile should be x-3, 3rd pile should be x*3, 4th pile should be x/3.
Do you know how much `x` is? `x` should be 9, because:
```
(9 + 3) + (9 - 3) + (9 * 3) + (9 / 3) = 12 + 6 + 27 + 3 = 48
```
So, 48 apples should be divided into `12, 6, 27, 3`.

## Task

Implement a function that accepts two argument, `n` and `y`, and returns the number of apples in each pile as described above. Each resulting number should be a positive integer. If there's no way to divide the apples, return an empty array/empty value (refer to the function declaration and test cases in your language of choice to see which option is relevant for you).

## Examples

```
n = 48
y = 3
result = [12, 6, 27, 3]

n = 100
y = 4
result = [20, 12, 64, 4]

n = 24
y = 4
result = []  (no way to divide the apples)

n = 25
y = 4
result = []  ([8,0,16,1] is not a correct answer since you can't have empty piles)
```
