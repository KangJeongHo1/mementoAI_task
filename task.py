def solution(phone_number):
    length = len(phone_number)
    masked_number = '*' * (length - 4) + phone_number[-4:]
    return masked_number

# 사용자 입력 받기
user_input = input("전화번호를 입력하세요: ")

# 길이 제한 조건 확인
if 4 <= len(user_input) <= 20:
    print(solution(user_input))
else:
    print("전화번호는 4자 이상 20자 이하이어야 합니다.")