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

Start by finding the middle floor between the top and bottom floors.
Then drop an egg from that floor.
If the egg breaks then find the middle floor between the lowest floor and the floor you are on now and drop an egg
If the egg doesn't break then find the middle floor between the floor you are on now and the top floor and drop an egg
Continue this process until the highest floor where an egg can be dropped without breaking is determined.

The time for this is O(log n) because you are eliminating halve of the amount of floors you have to check each time you move to another floor and drop an egg.
