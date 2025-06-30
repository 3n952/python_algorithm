# 이코테 문제 풀이: 숫자 카드 게임

class solutions(object):
    
    def solutions(self, *args, **kwargs):
        """
        숫자 카드 게임
        n: 행 개수
        m: 열의 개수  
        array: 2차원 숫자 배열
        """
        # kwargs에서 모든 값을 가져오도록 통일
        n = kwargs['n']
        m = kwargs['m']
        array = kwargs['array']
        
        # 각 행에서 가장 작은 수를 찾기
        min_values = []
        for row in array:
            min_values.append(min(row))

        return max(min_values)  # 그 중 제일 큰 값

        
        
