# 계산기 만들기
# 함수: 덧셈, 뺄셈, 메인

def add(x,y):
    return x+y


def sub(x,y):
    return x-y


while True:
    print("** 덧셈뺄셈 계산기 **")
    num1 = int(input("수1: "))
    pm = input("연산자: ")
    num2 = int(input("수2: "))

    if pm == "+":
        result = add(num1,num2)
    elif pm == "-":
        result = sub(num1,num2)
    print(f"계산: {num1} {pm} {num2} = {result}")

