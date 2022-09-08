Objective
In this challenge, we practice calculating standard deviation. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of  decimal place (i.e.,  format). An error margin of  will be tolerated for the standard deviation.

Example

The sum of the array values is  and there are  elements. The mean is .
Subtract the mean from each element, square each result, and take their sum.






Their sum is 18. Take the square root of  to get , the standard deviation.

Function Description

Complete the stdDev function in the editor below.

stdDev has the following parameters:
- int arr[n]: an array of integers

Prints
- float: the standard deviation to 1 place after the decimal

Input Format

The first line contains an integer, , denoting the size of arr.
The second line contains  space-separated integers that describe .

Constraints

Output Format

Print the standard deviation on a new line, rounded to a scale of  decimal place (i.e.,  format).

Sample Input

STDIN           Function
-----           --------
5               arr[] size n = 5
10 40 30 50 20  arr =[10, 40, 30, 50, 20]
Sample Output

14.1
Explanation

First, find the mean:

Next, calculate the squared distance from the mean, , for each :

Now compute , so:
