'''
https://leetcode.com/problems/most-common-word/description/

Q:금지된 단어를 제외한 가장 흥하게 등장하는 단어를 출력.대소문자 구분을 하지 않으며, 구두점 또한 무시

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"

Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

'''
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        # 금지 리스트 제외 모든 단어를 리스트로 만듦
        word = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        idx_counts = 0
        idx_list = []
        for idx in word:
            counts = word.count(idx)
            if counts >= idx_counts:
                idx_list = []
                idx_list.append(idx)
                idx_counts = counts
            else:
                pass
        
        return idx_list.pop()





