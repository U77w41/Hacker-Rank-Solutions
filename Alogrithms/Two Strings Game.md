Consider the following game for two players:

There are two strings A and B. Initially, some strings A' and B' are written on the sheet of paper. A' is always a substring of A and B' is always a substring of B. A move consists of appending a letter to exactly one of these strings: either to A' or to B'. After the move the constraint of A' being a substring of A and B' is a substring of B should still be satisfied. Players take their moves alternately. We call a pair (A', B') a position.

Two players are playing this game optimally. That means that if a player has a move that leads to his/her victory, he/she will definitely use this move. If a player is unable to make a move, he loses.

Alice and Bob are playing this game. Alice makes the first move. As always, she wants to win and this time she does a clever trick. She wants the starting position to be the Kth lexicographically winning position for the first player (i.e. her). Consider two positions (A'1, B'1) and (A'2, B'2). We consider the first position lexicographically smaller than the second if A1 is lexicographically smaller than A2, or if A1 is equal to A2 and B1 is lexicographically smaller than B2.

Please help her to find such a position, knowing the strings A, B and the integer K.

Note: An empty string has higher precedence than character "a"

Input Format

The first line of input consists of three integers, separated by a single space: N, M and K denoting the length of A, the length of B and K respectively. The second line consists of N small latin letters, corresponding to the string A. The third line consists of M small latin letters, corresponding to the string B.

Constraints

1 <= N, M <= 3 * 105
1 <= K <= 1018

Output Format

Output A' on the first line of input and B' on the second line of input. Please, pay attention that some of these strings can be empty. If there's no such pair, output "no solution" without quotes.

Sample Input 0

2 1 3
ab
c
Sample Output 0

a
c
Explanation 0

The given strings are  and . So there are  =  ways to fill a starting position (each character has two options, either to be present or not present).

 ["", ""] : If this is the start position, Alice will append  to . So, the next two moves will consist of appending  and  to  and  respectively. So, Bob will suffer lack of moves and hence Alice wins.

 ["", "c"] : If this is the start position, Alice will append  to . Now, Bob will suffer lack of moves and hence Alice wins.

 ["a", ""] : If Alice appends  to  then Bob will append  to  and if Alice appends  to  then Bob will append  to . So Alices looses.

 ["a", "c"] : If this is the start position, Alice will append  to . Now, Bob will suffer lack of moves and hence Alice wins.

 ["ab", ""] : If this is the start position, Alice will append  to . Now, Bob will suffer lack of moves and hence Alice wins.

 ["ab", "c"] : If this is the start position, Alice will suffer lack of moves and hence he looses.

 ["b", ""] : If this is the start position, Alice will append  to . Now, Bob will suffer lack of moves and hence Alice wins.

 ["b", "c"] : If this is the start position, Alice will suffer lack of moves and hence he looses.

So, the list of start positions in lexicographical order where Alice wins are: ["", ""], ["", "c"], ["a", "c"], ["ab", ""], ["b", ""]. The  one in this list is ["a", "c"].