# Friendly Pairs I

 - URL:[https://www.codewars.com/kata/59974515b4c40be3cc000263](https://www.codewars.com/kata/59974515b4c40be3cc000263)
 - Id: 59974515b4c40be3cc000263
 - Language: python
 - Completed on: 2017-10-19T09:02:35.133Z
 - Tags: Number Theory,Mathematics,Algorithms
 - Description:
The Abundancy (A) of a number `n` is defined as:

## (sum of divisors of n) / n

For example:
```python
A(8) = (1 + 2 + 4 + 8) / 8 = 15/8

A(25) = (1 + 5 + 25) / 25  = 31/25
```

Friendly Pairs are pairs of numbers (m, n), such that their abundancies are equal: A(n) = A(m).

Write a function that returns `"Friendly!"` if the two given numbers are a Friendly Pair. Otherwise return their respective abundacies as strings separated by a space, e.g. `"1 15/8"`

Notes:

- All fractions must be written in their most reduced form (e.g. `2/3` instead of `8/12`)
- Every number that is being checked is under 2400 
- Floats should be left on without rounding when you compare the abundancies of the two numbers


## Examples

```python
n = 6, m = 28 ==> "Friendly!"

n = 3, m = 9  ==> "4/3 13/9"
```
