# 이코테 문제 풀이: 1이 될 때까지

class solutions(object):
    
    def solutions(self, *args, **kwargs):
        """
        1이 될 때까지
        n: 자연수 입력값
        k: 자연수 나누는 값
        """
        # kwargs에서 모든 값을 가져오도록 통일
        n = kwargs['n']
        k = kwargs['k']
        
        count = 0
        while n != 1:
            if n % k == 0:
                n = n // k
            else:
                n = n - 1
            count += 1
        return count
        
        
