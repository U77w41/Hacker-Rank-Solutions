Victor is building a Japanese rock garden in his  square courtyard. He overlaid the courtyard with a Cartesian coordinate system so that any point  in the courtyard has coordinates  and . Victor wants to place  stones in the garden according to the following rules:

The center of each stone is located at some point , where  and  are integers .
The coordinates of all twelve stones are pairwise distinct.
The Euclidean distance from the center of any stone to the origin is not an integer.
The sum of Euclidean distances between all twelve points and the origin is an almost integer, meaning the absolute difference between this sum and an integer must be .
Given the values of  and  for the first stone Victor placed in the garden, place the remaining  stones according to the requirements above. For each stone you place, print two space-separated integers on a new line describing the respective  and  coordinates of the stone's location.

Input Format

Two space-separated integers describing the respective values of  and  for the first stone's location.

Constraints

Output Format

Print  lines, where each line contains two space-separated integers describing the respective values of  and  for a stone's location.

Sample Input 0

7 11
Sample Output 0

11 1
-2 12
5 4
12 -3
10 3
9 6
-12 -7
1 11
-6 -6
12 -4
4 12
Explanation 0

The diagram below depicts the placement of each stone and maps its distance to the origin (note that red denotes the first stone placed by Victor and blue denotes the eleven remaining stones we placed):

image

Now, let's determine if the sum of these distances is an almost integer. First, we find the distance from the origin to the stone Victor placed at , which is . Next, we calculate the distances for the remaining stones we placed in the graph above:

When we sum these eleven distances with the distance for the stone Victor placed, we get . The nearest integer to this number is , and the distance between this sum and the nearest integer is  (meaning it's an almost integer). Because this configuration satisfies all of Victor's rules for his rock garden, we print eleven lines of x y coordinates describing the locations of the stones we placed.