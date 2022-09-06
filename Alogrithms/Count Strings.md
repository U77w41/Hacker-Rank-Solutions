A regular expression is used to describe a set of strings. For this problem the alphabet is limited to 'a' and 'b'.

We define  to be a valid regular expression if:
1)  is "" or "".
2)  is of the form "", where  and  are regular expressions.
3)  is of the form "" where  and  are regular expressions.
4)  is of the form "" where  is a regular expression.

Regular expressions can be nested and will always have have two elements in the parentheses. ('' is an element, '' is not; basically, there will always be pairwise evaluation) Additionally, '' will always be the second element; '' is invalid.

The set of strings recognized by  are as follows:
1) If  is "", then the set of strings recognized .
2) If  is "", then the set of strings recognized .
3) If  is of the form "" then the set of strings recognized = all strings which can be obtained by a concatenation of strings  and , where  is recognized by  and  by .
4) If  is of the form "" then the set of strings recognized = union of the set of strings recognized by  and .
5) If  is of the form "" then the the strings recognized are the empty string and the concatenation of an arbitrary number of copies of any string recognized by .

Task
Given a regular expression and an integer, , count how many strings of length  are recognized by it.

Input Format

The first line contains the number of test cases .  test cases follow.
Each test case contains a regular expression, , and an integer, .

Constraints

It is guaranteed that  will conform to the definition provided above.
Output Format

Print  lines, one corresponding to each test case containing the required answer for the corresponding test case. As the answers can be very big, output them modulo .

Sample Input

3  
((ab)|(ba)) 2  
((a|b)*) 5  
((a*)(b(a*))) 100
Sample Output

2  
32  
100
Explanation

For the first case, the only strings recognized are "" and "". Of the  possible strings of length ,  of them fit that expression.
For the second case, the RegEx recognizes any string of any length containing only 's and 's. The number of strings of length  recognized by this expression is .
For the third case, the RegEx recognizes any string having one , preceeded and followed by any number of 's. There are  strings of length  which have a single  in them.