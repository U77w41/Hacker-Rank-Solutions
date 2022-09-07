A border of a string is a proper prefix of it that is also a suffix. For example:

a and abra are borders of abracadabra,
kan and kankan are borders of kankankan.
de is a border of decode.
Note that decode is not a border of decode because it's not proper.

A palindromic border is a border that is palindromic. For example,

a and ana are palindromic borders of anabanana,
l, lol and lolol are palindromic borders of lololol.
Let's define  as the number of palindromic borders of string . For example, if  lololol, then .

Now, a string of length  has exactly  non-empty substrings (we count substrings as distinct if they are of different lengths or are in different positions, even if they are the same string). Given a string , consisting only of the first 8 lowercase letters of the English alphabet, your task is to find the sum of  for all the non-empty substrings  of . In other words, you need to find:

where  is the substring of  starting at position  and ending at position .
Since the answer can be very large, output the answer modulo .

Input Format

The first line contains a string consisting of  characters.

Output Format

Print a single integer: the remainder of the division of the resulting number by .

Constraints


All characters in the string can be any of the first 8 lowercase letters of the English alphabet (abcdefgh).

Sample Input 1

ababa
Sample Output 1

5
Sample Input 2

aaaa
Sample Output 2

10
Sample Input 3

abcacb
Sample Output 3

3
Explanation

 ababa has 15 substrings but only 4 substrings have palindromic borders.

 aba 
 ababa 
 bab 
 aba 