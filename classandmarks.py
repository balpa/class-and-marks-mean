import random


class Person:
    def __init__(
        self, name: str, age: int, hair_color: str, loves_shibari: bool, mark: int
    ) -> None:
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.loves_shibari = loves_shibari
        self.mark = mark

    def changeShibariSituation(self, x: bool):
        self.loves_shibari = x


class Classroom:
    def __init__(self, class_no: int, students: list, teacher: Person) -> None:
        self.class_no = class_no
        self.students = students
        self.teacher = teacher

    def calculateAverageMark(self) -> float:
        result = 0
        for x in range(len(self.students)):
            result += self.students[x].mark
        return result / len(self.students)


names = [
    "Berke",
    "James",
    "Mary",
    "Jane",
    "Joe",
    "Jim",
    "Jeff",
    "Jimmy",
    "James",
    "Michael",
    "William",
    "Linda",
    "Elizabeth",
    "Barbara",
    "Jessica",
    "Mary",
    "Sarah" "Karen",
    "Nancy",
]
hair_colors = ["black", "brown", "blond", "red", "white"]

classroom = Classroom(1, [], Person("Berke", 26, "black", True, 100))

for x in range(20):
    name = random.choice(names)
    age = random.randint(18, 30)
    hair_color = random.choice(hair_colors)
    loves_shibari = random.choice([True, False])
    mark = random.randint(1, 100)
    person = Person(name, age, hair_color, loves_shibari, mark)
    classroom.students.append(person)

print("***************")
print("               ")
for x in range(len(classroom.students)):
    print(classroom.students[x].name, " --- ", classroom.students[x].mark)
print("               ")
print("***************")

print(Classroom.calculateAverageMark(classroom))
