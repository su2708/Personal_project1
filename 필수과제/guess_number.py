import random

# 랜덤 숫자와 입력한 숫자의 크기를 비교하는 함수
def compare_numbers(target, guess):
    if target > guess:
        return '랜덤 숫자보다 작습니다. 다시 입력하세요.'
    elif target < guess:
        return '랜덤 숫자보다 큽니다. 다시 입력하세요.'
    else:
        return '정답입니다!'

def main():
    target_number = random.randint(1, 10)
    print("행운의 랜덤 숫자를 맞혀보세요! 랜덤 숫자는 1 이상 10 이하입니다.")
    
    while True:
        guess_number = int(input('예상 숫자: '))
        result = compare_numbers(target_number, guess_number)
        print(result)
        
        # 정답인 경우 반복문 탈출
        if '정답' in result:
            break

if __name__ == "__main__":
    main()