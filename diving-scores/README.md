# Diving Scores

 - URL:[https://www.codewars.com/kata/5c97be7d856e611dbb78805f](https://www.codewars.com/kata/5c97be7d856e611dbb78805f)
 - Id: 5c97be7d856e611dbb78805f
 - Language: javascript
 - Completed on: 2022-06-23T12:48:21.968Z
 - Tags: Fundamentals,Algorithms
 - Description:
# Description

For this Kata you will need to create a function which works out the score of a dive in an Olympic diving competition and displays it in the correct format. The function will take 2 arguments:

- An array of numbers representing the judges' scores, called `scores`
- A number representing the degree of difficulty of the dive, called `tariff`

The 2 lowest and 2 highest scores by the judges are discarded and the 3 remaining scores are added together. The result of this is then multiplied by the difficulty ( `tariff` ) to get the score for the dive.

https://www.britannica.com/story/how-is-diving-scored

**The answer should be a string, and should always have exactly 2 digits after the decimal point, as this is how diving scores are displayed.**

# Note

The `scores` will only contain numbers between `0` and `10` and the `tariff` will always be greater than `0`.

# Example

```javascript
scoreOfDive( [ 7, 7.5, 8, 7.5, 6, 7, 7 ], 3 )  =>  '64.50'
```
