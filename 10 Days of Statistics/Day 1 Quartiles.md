Objective
In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.

Example

The sorted array is  which has an odd number of elements. The lower half consists of , and its median is . The middle element is  and represents the second quartile. The upper half is  and its median is . Return .


The array is already sorted. The lower half is  with a median = . The median of the entire array is , and of the upper half is . Return .

Function Description

Complete the quartiles function in the editor below.

quartiles has the following parameters:

int arr[n]: the values to segregate
Returns

int[3]: the medians of the left half of ,  in total, and the right half of .
Input Format

The first line contains an integer, , the number of elements in .
The second line contains  space-separated integers, each an .

Constraints

, where  is the  element of the array.
Sample Input

STDIN                   Function
-----                   --------    
9                       arr[] size n = 9 
3 7 8 5 12 14 21 13 18  arr = [3, 7, 8, 5, 12, 14, 21, 13,18]
Sample Output

6
12
16
Explanation

. There is an odd number of elements, and the middle element, the median, is .

As there are an odd number of data points, we do not include the median (the central value in the ordered list) in either half:

Lower half (L): 3, 5, 7, 8

Upper half (U): 13, 14, 18, 21

Now find the quartiles:

 is the . So, .
 is the . So, .
 is the . So, .