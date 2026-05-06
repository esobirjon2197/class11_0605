
# 21-m
class Player:
    def __init__(self, health, damage):
        self._health = health
        self.__damage = damage

    def hit(self):
        self._health -= self.__damage

    def heal(self, x):
        self._health += x

    def info(self):
        print(f"Health:{self._health}")


pl1 = Player(100, 30)

pl1.hit()
pl1.info()

pl1.heal(20)
pl1.info()


# 22-m
class Teacher:
    def __init__(self, subject):
        self._subject = subject

    def teach(self):
        print("Teaching...")

    def add_course(self):
        print("Course added")


t1 = Teacher("Math")

t1.teach()
t1.add_course()
