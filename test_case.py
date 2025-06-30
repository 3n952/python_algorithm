# test_case.py
"""
테스트 케이스 자동 실행 스크립트

이 파일은 지정한 모듈의 클래스를 임포트하여, 특정 함수에 입력값을 전달하고 결과를 검증하는 테스트 자동화 도구입니다. 
테스트 결과로 정답 여부, 실행 결과, 예상 결과, 실행 시간을 출력합니다.

사용법:
    python test_case.py --fname <테스트할_모듈명>

주의 사항:
1. --fname: 테스트할 파이썬 파일명(확장자 .py 제외)
2. test_cases_data: 테스트 케이스들의 입력값과 기대 결과를 직접 수정하여 사용
   - 각 케이스는 (input_data, expected_result) 튜플 형태
"""

import time
import argparse
import importlib

import case_collector as cfg

def args_parser():
    parser = argparse.ArgumentParser(description="테스트 케이스 실행 파라미터")
    parser.add_argument("--fname", type=str, required=True, help="테스트 케이스 파일명")
    return parser.parse_args()

def run_test_case(module_name, class_name, func_name, args, expected, case_num):
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
    print(f"[{module_name}.py] 테스트 케이스 {case_num} 실행 중..:")
    print(f"정답 여부: {'정답' if is_correct else '오답'}")
    if not is_correct:
        print(f"실행 결과: {result} <-> 예상 결과: {expected}")
    print(f"실행 시간: {elapsed:.6f}초\n")
    return is_correct

if __name__ == "__main__":

    # 건들지 말 것
    #########################################################

    args = args_parser()
    input_case = args.fname.upper()
    try:
        test_cases_data = getattr(cfg, input_case)
    except AttributeError:
        raise ValueError(f"config.py에 '{input_case}' 변수가 존재하지 않습니다.")
    
    if not test_cases_data:
        raise ValueError("테스트 케이스가 설정되지 않았습니다. test_cases_data를 확인하세요.")

    all_correct = True
    total_cases = len(test_cases_data)
    passed_cases = 0
    
    for i, (input_data, expected_result) in enumerate(test_cases_data, 1):
        if run_test_case(args.fname, "solutions", "solutions", input_data, expected_result, i):
            passed_cases += 1
        else:
            all_correct = False
    
    print("--------------------------------")
    print(f"전체 테스트 결과: {passed_cases}/{total_cases} 케이스 통과")
    
    if all_correct:
        print("무야호! 모든 테스트 케이스 통과!")
    else:
        print("일부 테스트 케이스 실패 ㅜㅜ") 