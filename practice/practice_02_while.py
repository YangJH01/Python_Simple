# 문제1) 로그인(pw) -> 3번 이상 암호를 틀리면 프로그램 종료!

# pw = 1234
# count = 0
# while True:
#     if count >= 3:
#         print("종료: 암호를 3회이상 틀리셨습니다")
#         break
#     input_pw = int(input("암호: "))
#     if pw == input_pw:
#         print("반갑습니다.")
#         break
#     else:
#         print("경고: 올바른 암호를 입력해주세요.")
#         count += 1

# 문제2) 1~100까지 더해서 총합을 계산하세요.
# - for문
_sum = 0
for i in range(1, 101):
    _sum += i
print(f"총합:{_sum}")

# - while문
i = 1
__sum = 0
while i < 101 :
    __sum += i
    i += 1
print(f"총합:{__sum}")

while True:
    i += 1
    if i>= 101:
        break
    __sum += i
print(f"총합(교수님ver):{__sum}")