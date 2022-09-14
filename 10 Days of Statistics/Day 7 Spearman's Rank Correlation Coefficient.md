Objective
In this challenge, we practice calculating Spearman's rank correlation coefficient. Check out the Tutorial tab for learning materials!

Task
Given two -element data sets,  and , calculate the value of Spearman's rank correlation coefficient.

Input Format

The first line contains an integer, , denoting the number of values in data sets  and .
The second line contains  space-separated real numbers (scaled to at most one decimal place) denoting data set .
The third line contains  space-separated real numbers (scaled to at most one decimal place) denoting data set .

Constraints

, where  is the  value of data set .
, where  is the  value of data set .
Data set  contains unique values.
Data set  contains unique values.
Output Format

Print the value of the Spearman's rank correlation coefficient, rounded to a scale of  decimal places.

Sample Input

10
10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
200 44 32 24 22 17 15 12 8 4
Sample Output

0.903
Explanation

We know that data sets  and  both contain unique values, so the rank of each value in each data set is unique. Because of this property, we can use the following formula to calculate the value of Spearman's rank correlation coefficient:

Here,  is the difference between ranks of each pair . The following table shows the calculation of :


Now, we find the value of the coefficient:

When rounded to a scale of three decimal places, we get  as our final answer.