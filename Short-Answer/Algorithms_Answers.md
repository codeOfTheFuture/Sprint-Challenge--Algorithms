#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(n)
Each time the while loop runs, n squared is being added to the value a until the value a is equal to n cubed. As the value of n increase the amount of loops that run increase at a liner rate.

b)
O(n log n)
The outer for loop is iterating n times so the time for the outer loop is 0(n). In the while loop the value of j is being doubled each time it runs and incrementing the sum by one. Since j is being doubled each time the number of times the loop runs will be halved even as n grows. The time for the while loop is O(log n).

c)
0(n)
bunnyEars is being called recursively and subtracting one from the number of bunnies that is passed in until the number of bunnies is zero. So the number of bunnies will determine how many times the function is called recursively. Then once each function call is returned, 2 is added each time to the number of bunnies being return from the function. The number of times this operation happens will also increase as the number of bunnies increases.

## Exercise II
