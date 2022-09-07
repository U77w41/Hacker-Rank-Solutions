A number is algebraic if it is a root of some nonzero polynomial with integer coefficients. A number is transcendental if it is not algebraic.

For example, , ,  and  (golden ratio) are algebraic, because they are roots of , ,  and , respectively. Also, it can be shown that the sum and product of two algebraic numbers is also algebraic, so for example ,  and  are also algebraic. However, it has been shown by Lindemann that  is transcendental.

The degree of an algebraic number is the minimal degree of a polynomial with integer coefficients in which it is a root. For example, the degrees of , ,  and  are , ,  and , respectively.

Given  positive integers , , ..., , calculate the degree of the following algebraic number:

Input Format
The first line of input contains , the number of test cases. The descriptions of the test cases follow.

Each test case has two lines of input. The first line contains a single integer, . The second line contains  integers , ...,  separated by single spaces.

Output Format
For each test case, output one line containing exactly one integer, which is the answer for that test case.

Constraints



The sum of the 's in a single test file is at most 

Sample Input

3
1
4
3
2 4 4
4
1 2 3 5
Sample Output

1
2
8
Explanation
Case 1: A minimal polynomial of  is .

Case 2: A minimal polynomial of  is .

Case 3: A minimal polynomial of  is:

