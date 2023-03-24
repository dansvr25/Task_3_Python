class Applicant:
    def __init__(self, name, russian, math, physics):
        self.name = name
        self.russian = russian
        self.math = math
        self.physics = physics

    def to_string(self): # Складываю значения атрибутов объекта
        return self.name + ', ' + str(self.russian) + ', ' + str(self.math) + ', ' + str(self.physics)


def select_students(applicants, n):
    # Сортирую абитуриентов по сумме баллов, потом уже по математике и физике
    sorted_applicants = sorted(applicants, key=lambda x: (-(x.russian + x.math + x.physics), -x.math, -x.physics))

    # Возвращается с нулевого до n-го студента (тех, кто проходит по баллам)
    selected_applicants = sorted_applicants[0:n]

    return selected_applicants


# Создаю пустой лист для студентов из файла
applicants = []

# Считываю студентов из файла
with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()
    for line in lines:
        arr = [str(param) for param in line.split(",")]
        student = Applicant(arr[0], int(arr[1]), int(arr[2]), int(arr[3]))
        applicants.append(student)

selected_applicants = select_students(applicants, 3)

# Записываю студентов в файл
with open('output.txt', 'w') as outputFile:
    for i in selected_applicants:
        outputFile.write(i.to_string() + '\n')
