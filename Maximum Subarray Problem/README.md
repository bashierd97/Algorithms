## This is a program that implemenets both the brute-force and recursive algorithms for the [Maximum Subarray Problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem#:~:text=If%20the%20array%20contains%20all,%2C%20if%20it%20is%20permitted).

For the array size, I used an array of size 1000 with values randomized ranging from -50 to 50.

For the graph, as you can see Brute Force grows in an exponential fashion O(n^2), while Recursive Method grows as O(n*lgn). At a problem size around 90 - 180 (from test trials I've ran with my program, it varies because of the values inside the array and how everytime it's randomized) the recursive algorithm beats my brute-force algorithm. 

I've included two graphs, one that shows a more smooth graph (using less accurate timing functions) and another one that shows a far more accurate timing but not as appealing graph. 
