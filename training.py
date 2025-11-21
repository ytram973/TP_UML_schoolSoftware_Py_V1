from datetime import date

class Training:
    # Constructor
    def __init__(self, training_name: str, start_date: date, end_date: date):
        self.validate_dates(start_date, end_date)
        self.training_name = training_name
        self.start_date = start_date
        self.end_date = end_date
        self.students = []
        self.lessons = []

    # Validation method
    def validate_dates(self, start: date, end: date):
        if start > end:
            raise ValueError("La date de début ne peut pas être après la date de fin.")

    # Getters and Setters
    def set_training_name(self, training_name: str):
        self.training_name = training_name

    def get_training_name(self) -> str:
        return self.training_name

    def set_start_date(self, start_date: date):
        self.validate_dates(start_date, self.end_date)
        self.start_date = start_date

    def get_start_date(self) -> date:
        return self.start_date

    def set_end_date(self, end_date: date):
        self.validate_dates(self.start_date, end_date)
        self.end_date = end_date

    def get_end_date(self) -> date:
        return self.end_date

    # Manage students
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def get_students(self):
        return list(self.students)

    # Manage lessons
    def add_lesson(self, lesson):
        if lesson not in self.lessons:
            self.lessons.append(lesson)

    def remove_lesson(self, lesson):
        if lesson in self.lessons:
            self.lessons.remove(lesson)

    def get_lessons(self):
        return list(self.lessons)

    # String representation
    def __str__(self):
        return (f"Training Name: {self.training_name}, "
                f"Start Date: {self.start_date.strftime('%d/%m/%Y')}, "
                f"End Date: {self.end_date.strftime('%d/%m/%Y')}")


# Exemple d’utilisation (comme ton main en Java)
if __name__ == "__main__":
    training = Training(
        "Python Basics",
        date(2024, 7, 1),
        date(2025, 7, 15)
    )
    print(training)
