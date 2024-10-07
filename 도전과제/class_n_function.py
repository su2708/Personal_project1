class Person:
    def __init__(self, name: str, gender: str, age: int):
        self.name: str = name
        self.gender: str = gender
        self.age: int = age
        
    def display(self):
        print(f'이름: {self.name}, 성별: {self.gender}')
        print(f'나이: {self.age}')
        
    # 나잇대에 맞는 인사
    def greet(self):
        if self.age < 20:
            print(f'안녕하세요, {self.name}! 미성년이시군요!')
        else:
            print(f'안녕하세요, {self.name}! 성인이시군요!')
        
def main():
    age = int(input('나이: '))
    name = input('이름: ')
    
    # 성별 입력이 'male' 또는 'female'일 때까지 반복
    while True:
        gender = input('성별: ')
        if gender == 'male' or gender == 'female':
            break
        else:
            print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")
    
    person = Person(name, gender, age)
    person.display()
    person.greet()

if __name__ == '__main__':
    main()