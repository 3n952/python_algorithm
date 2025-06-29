# test_case.py
"""
테스트 케이스 자동 실행 스크립트

이 파일은 지정한 모듈의 클래스를 임포트하여, 특정 함수에 입력값을 전달하고 결과를 검증하는 테스트 자동화 도구입니다. 
테스트 결과로 정답 여부, 실행 결과, 예상 결과, 실행 시간을 출력합니다.

사용법:
    python test_case.py --fname <테스트할_모듈명>

주의 사항:
1. --fname: 테스트할 파이썬 파일명(확장자 .py 제외)
2. input_data, result: 테스트 입력값과 기대 결과를 직접 수정하여 사용
"""

import time
import argparse
import importlib


def args_parser():
    parser = argparse.ArgumentParser(description="테스트 케이스 실행 파라미터")
    parser.add_argument("--fname", type=str, required=True, help="테스트 케이스 파일명")
    return parser.parse_args()

def run_test_case(module_name, class_name, func_name, args, expected):
    module = importlib.import_module(module_name)
    cls = getattr(module, class_name)
    inst = cls()
    func = getattr(inst, func_name)
    start = time.time()

    try:
        result = func(*args)
    except:
        result = func(**args)
        
    end = time.time()
    elapsed = end - start
    is_correct = result == expected
    print(f"[{module_name}.py] 실행 중..:")
    print(f"정답 여부: {'정답' if is_correct else '오답'}")
    if not is_correct:
        print(f"실행 결과: {result} <-> 예상 결과: {expected}")
    print(f"실행 시간: {elapsed:.6f}초\n")
    return is_correct

if __name__ == "__main__":
    # 입력설정 !!!!
    args = args_parser()
    input_data = {'n': 5, 'm': 8, 'k': 3, 'array': [2, 4, 5, 4, 6]}  # case 인풋
    result = 46  # 정답
    

    # 건들지 말 것
    #########################################################
    if input_data is None or result is None:
        raise ValueError("입력설정을 잘 확인하거라(input_data, results 확인)")

    test_cases = [
        (args.fname, "solutions", "solutions", input_data, result),
    ]
    all_correct = True
    for module_name, class_name, func_name, args, expected in test_cases:
        if not run_test_case(module_name, class_name, func_name, args, expected):
            all_correct = False
    if all_correct:
        print("--------------------------------")
        print("테스트 케이스 통과 !")
    else:
        print("--------------------------------")
        print("테스트 통과 실패 ㅜㅜ") 