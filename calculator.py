"""
사칙연산 계산기 프로그램
덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 계산기
"""

def add(a, b):
    """덧셈 함수"""
    return a + b

def subtract(a, b):
    """뺄셈 함수"""
    return a - b

def multiply(a, b):
    """곱셈 함수"""
    return a * b

def divide(a, b):
    """나눗셈 함수"""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다!")
    return a / b

def calculator():
    """메인 계산기 함수"""
    print("=" * 40)
    print("사칙연산 계산기")
    print("=" * 40)
    print("연산 종류:")
    print("1. 덧셈 (+)")
    print("2. 뺄셈 (-)")
    print("3. 곱셈 (*)")
    print("4. 나눗셈 (/)")
    print("=" * 40)
    
    try:
        # 첫 번째 숫자 입력
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        
        # 연산자 선택
        operation = input("연산자를 선택하세요 (+, -, *, /): ")
        
        # 두 번째 숫자 입력
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        
        # 연산 수행
        if operation == '+':
            result = add(num1, num2)
            print(f"\n결과: {num1} + {num2} = {result}")
        elif operation == '-':
            result = subtract(num1, num2)
            print(f"\n결과: {num1} - {num2} = {result}")
        elif operation == '*':
            result = multiply(num1, num2)
            print(f"\n결과: {num1} * {num2} = {result}")
        elif operation == '/':
            result = divide(num1, num2)
            print(f"\n결과: {num1} / {num2} = {result}")
        else:
            print("잘못된 연산자입니다. +, -, *, / 중 하나를 선택하세요.")
            
    except ValueError as e:
        print(f"오류: {e}")
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    calculator()

