# Shopping List

 - URL:[https://www.codewars.com/kata/596266482f9add20f70001fc](https://www.codewars.com/kata/596266482f9add20f70001fc)
 - Id: 596266482f9add20f70001fc
 - Language: javascript
 - Completed on: 2017-08-06T21:32:30.516Z
 - Tags: Algorithms,Fundamentals,Arrays
 - Description:
Calculate the cost of a shopping list by writing a function. The function takes an argument which is an array consisting of sub-arrays. For example:

```javascript
shoppingListCost([["Orange Juice", 2],["Chocolate", 4],["Pears", 8]]) 
```
The input array includes sub arrays containing the name and quantity of each item being purchased. Already existing in the global scope is an object which gives some information regarding the shopping items: 

```javascript
var groceries = {
  "Orange Juice": {
      "price" : 1.5,
      "discount": 10, 
      "bogof": false
  },
    
  "Chocolate": {
      "price" : 2,
      "discount" : 0,
      "bogof": true
  },
  
  // more items...
}
  
  ```
  
This object contains the price of the item, the discount currently being offered on that item, and whether the item is currently "buy one get one free" (meaning for every item purchased, one of the same item is free). 

Return the cost of the shopping list. If the input array contains no items, return zero. Round the answer to 2 decimal places. 

All input arrays will be valid and contain items included in the global groceries object. Each item will only appear once in any input array. 
  





Examples

```javascript
shoppingListCost([["Orange Juice", 2],["Chocolate", 4]]) 
```
returns 6.7

```javascript
shoppingListCost([["Chocolate", 5],["Orange Juice", 15]])
```
returns 26.25


