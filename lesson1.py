import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_chill(self):
        print("Rest time")
        self.progress -= 0.10
        self.gladness += 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')

    def live(self, day):
        day = f'Day {day} of {self.name} life'
        print(f'{day:=^50}')
        liveCube = random.randint(1,3)
        if liveCube == 1:
            self.to_study()
        elif liveCube == 2:
            self.to_sleep()
        elif liveCube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

human = Student(input('Enter your name: '))
for i in range(1,366):
    if human.alive == False:
        break
    human.live(i)