# Simple Fun #83: MineSweeper

 - URL:[https://www.codewars.com/kata/58952e29f0902eae8b0000cb](https://www.codewars.com/kata/58952e29f0902eae8b0000cb)
 - Id: 58952e29f0902eae8b0000cb
 - Language: python
 - Completed on: 2017-09-15T11:16:15.551Z
 - Tags: Puzzles
 - Description:
# Task
 In the popular `Minesweeper` game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a `Minesweeper` game setup.

# Example

 For
```
matrix = [[true, false, false],
            [false, true, false],
            [false, false, false]]```
the output should be
```
minesweeper(matrix) = [[1, 2, 1],
                         [2, 1, 1],
                         [1, 1, 1]]```
Check out the image below for better understanding:

 ![](https://codefightsuserpics.s3.amazonaws.com/tasks/minesweeper/img/example.png?_tm=1474900981846)

# Input/Output


 - `[input]` 2D boolean array `matrix`

    A non-empty rectangular matrix consisting of boolean values - `true` if the corresponding cell contains a mine, `false` otherwise.

    Constraints:

    `2 ≤ matrix.length ≤ 10,`

    `2 ≤ matrix[0].length ≤ 10.`


 - `[output]` 2D integer array

    Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.
