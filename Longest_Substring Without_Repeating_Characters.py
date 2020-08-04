"""

Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict = []
        length = currLeng = 0
        
        for x in s:
            if x not in myDict:
                myDict.append(x)
                currLeng += 1
            else:
                myDict = myDict[myDict.index(x)+1:] + [x]
                length = max(length, currLeng)
                currLeng = len(myDict)
        
        return max(length, currLeng)