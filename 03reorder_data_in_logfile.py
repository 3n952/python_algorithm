''' 
https://leetcode.com/problems/reorder-data-in-log-files/description/

Q
1. 로그의 가장 앞 부분은 식별자
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
3. 식별자는 순서에 영향을 끼치지 않지만, 문가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
'''

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters, digits = [], []
        for log in logs:
            # 식별자 다음 로그가 숫자인 경우
            if log.split()[1].isdigit():
                digits.append(log)
            # 문자인 경우
            else:
                letters.append(log)
        
        # 식별자 다음 로그 기준으로 정렬, 그 로그가 동일하면 식별자로 순서 정렬
        letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))

        return letters + digits