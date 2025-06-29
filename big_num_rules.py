# 이코테 문제 풀이: 큰 수의 법칙

class solutions(object):
    
    def solutions(self, *args, **kwargs):
        """
        n: 배열의 크기
        m: 더하는 횟수
        k: 연속해서 더할 수 있는 최대 횟수
        numbers: 숫자 배열
        """
        n = kwargs['n']
        m = kwargs['m']
        k = kwargs['k']
        array = kwargs['array']

        if len(array) < n or len(array) > n:
            raise ValueError('문제 오류')
        
        else:
            array = sorted(array, reverse=True)
            first, second = array[0], array[1]
            fixed_idx = m // (k + 1)
            remained_idx = m % (k + 1)
            fixed_num = (first * fixed_idx * k) + (second * fixed_idx)
            remained_num = first * remained_idx

            return fixed_num + remained_num