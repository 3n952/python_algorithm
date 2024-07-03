'''
Q: 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하자. 단, 나눗셈 연산은 사용하지 말 것.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

class Solution(object):
    def productExceptSelf(self, nums):
        out = []
        p = 1

        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums)-1 , -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
