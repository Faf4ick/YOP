class School:
    def __init__(self, name, location, student_count):
        self.name = name
        self.location = location
        self.student_count = student_count

    def get_info(self):
        return f"{self.name} находиться {self.location} в школе учиться {self.student_count} ученика."

my_school = School("Лицей №23", "Кадининграде", 1583)
print(my_school.get_info())