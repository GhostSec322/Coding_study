class Monster:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print(f'나는 {self.name}이다 그리고{self.age}살이야')

shark=Monster('Shark',7)
shark.say()