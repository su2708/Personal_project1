class Person:
    def __init__(self, name: str, gender: str, age: int):
        self.name: str = name
        self.gender: str = gender
        self.age: int = age
        
    def display(self):
        print(f'이름: {self.name}, 성별: {self.gender}')
        print(f'나이: {self.age}')
        
def main():
    age = int(input('나이: '))
    name = input('이름: ')
    gender = input('성별: ')
    
    person = Person(name, gender, age)
    person.display()

if __name__ == '__main__':
    main()