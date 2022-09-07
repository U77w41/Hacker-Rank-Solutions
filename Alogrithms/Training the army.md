In the magical kingdom of Kasukabe, people strive to possess skillsets. Higher the number of skillset present among the people, the more content people will be.

There are  types of skill set present and initially there exists  people possessing  skill set, where .

There are  wizards in the kingdom and they have the ability to transform the skill set of a person into another skill set. Each of the these wizards has two lists of skill sets associated with them,  and . He can only transform the skill set of person whose initial skill set belongs to the list  to one of the final skill set which belongs to the list . That is, if  and  then following transformation can be done by that trainer.

Once a transformation is done, both skill is removed from the respective lists. In the above example, if he perform  transformation on a person, list  will be updated to  and list  will be . This updated list will be used for further transformations.

Few points to note are:

One person can possess only one skill set.
A wizard can perform zero or more transformation as long as they satisfies the above criteria.
A person can go through multiple transformation of skill set.
Same class transformation is also possible. That is a person' skill set can be transformed into his current skill set. Eg.  in the above example.
Your goal is to design a series of transformation which results into maximum number of skill set with non-zero number of people knowing it.

Input Format

The first line contains two numbers, , where  represent the number of skill set and  represent the number of wizards.
Next line contains  space separated integers, , where  represents the number of people with  skill. Then follows  lines, where each pair of line represent the configuration of each wizard.
First line of the pair will start with the length of list  and followed by list  in the same line. Similarly second line of the pair starts with the length of list  and then the list .

Constraints

Output Format

The output must consist of one number, the maximum number of distinct skill set that can the people of country learn, after making optimal transformation steps.

Sample Input

3 3
3 0 0
1 1
2 2 3
1 2
1 3
1 1
1 2 
Sample Output

2  
Explanation

There are  types of skill sets present along with  wizards. Initially, all three people know the  skill set but no one knows the  and  skill sets.

The  wizard's initial lists are:  and . Suppose, he performs  transformation one any one of person with the  skill set, then it's list  will be updated to an empty list  and list  will be .
Now, we have two people knowing the  skill set and one person knowing the  skill set.

The  wizard's initial lists are:  and . He will use the transformation  one of the person with the  skill set, then it's lists will also be updated to an empty lists A:  and : .

Now, we have 1 person with  skillset and and 2 people knowing the  skillset.

The  wizard's initial lists are:  and . He will transform one of the person with  skillset to  one using the transformation . It's lists will also be updated to an empty lists A:  and : .
At this point, no further transformations are possible and we have achieved our maximum possible answer. Thus, each of the skill set, is known by  person.. This means there are three skill sets available in the kingdom.