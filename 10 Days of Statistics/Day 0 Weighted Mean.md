Objective
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers and an array, , representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of  decimal place (i.e.,  format).

Example


The array of values . Their sum is . The sum of . The weighted mean is . Print  and return.

Function Description
Complete the weightedMean function in the editor below.

weightedMean has the following parameters:
- int X[N]: an array of values
- int W[N]: an array of weights

Prints
- float: the weighted mean to one decimal place

Input Format

The first line contains an integer, , the number of elements in arrays  and .
The second line contains  space-separated integers that descdribe the elements of array .
The third line contains  space-separated integers that descdribe the elements of array .

Constraints

, where  is the  element of array .
, where  is the  element of array .
Output Format

Print the weighted mean on a new line. Your answer should be rounded to a scale of  decimal place (i.e.,  format).

Sample Input

STDIN           Function
-----           --------
5               X[] and W[] size n = 5
10 40 30 50 20  X = [10, 40, 30, 50, 20]  
1 2 3 4 5       W = [1, 2, 3, 4, 5]
Sample Output

32.0
Explanation

We use the following formula to calculate the weighted mean:

And then print our result to a scale of  decimal place () on a new line.