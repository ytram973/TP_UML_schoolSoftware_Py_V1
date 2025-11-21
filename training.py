from datetime import date


class Training:
    """
    A class representing a training program with a name, start and end dates,
    associated students, and lessons.

    Attributes
    ----------
    training_name : str
        The name of the training program.
    start_date : date
        The start date of the training.
    end_date : date
        The end date of the training.
    students : list
        A list of students enrolled in the training.
    lessons : list
        A list of lessons included in the training.
    """

    def __init__(self, training_name: str, start_date: date, end_date: date):
        """
        Initialize a Training instance.

        Parameters
        ----------
        training_name : str
            The name of the training program.
        start_date : date
            The training start date.
        end_date : date
            The training end date.

        Raises
        ------
        ValueError
            If start_date is after end_date.
        """
        self.validate_dates(start_date, end_date)
        self.training_name = training_name
        self.start_date = start_date
        self.end_date = end_date
        self.students = []
        self.lessons = []

    def validate_dates(self, start: date, end: date):
        """
        Validate that the start date is not after the end date.

        Parameters
        ----------
        start : date
            The proposed start date.
        end : date
            The proposed end date.

        Raises
        ------
        ValueError
            If start > end.
        """
        if start > end:
            raise ValueError("La date de début ne peut pas être après la date de fin.")

    # Getters and Setters
    def set_training_name(self, training_name: str):
        """Set the name of the training program."""
        self.training_name = training_name

    def get_training_name(self) -> str:
        """Return the name of the training program."""
        return self.training_name

    def set_start_date(self, start_date: date):
        """
        Set the start date of the training.

        Raises
        ------
        ValueError
            If start_date > current end_date.
        """
        self.validate_dates(start_date, self.end_date)
        self.start_date = start_date

    def get_start_date(self) -> date:
        """Return the training start date."""
        return self.start_date

    def set_end_date(self, end_date: date):
        """
        Set the end date of the training.

        Raises
        ------
        ValueError
            If new end_date < current start_date.
        """
        self.validate_dates(self.start_date, end_date)
        self.end_date = end_date

    def get_end_date(self) -> date:
        """Return the training end date."""
        return self.end_date

    # Manage students
    def add_student(self, student):
        """
        Add a student to the training if they are not already enrolled.

        Parameters
        ----------
        student : any
            The student to add.
        """
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        """
        Remove a student from the training if they are enrolled.

        Parameters
        ----------
        student : any
            The student to remove.
        """
        if student in self.students:
            self.students.remove(student)

    def get_students(self):
        """
        Return a copy of the students list.

        Returns
        -------
        list
            A list of enrolled students.
        """
        return list(self.students)

    # Manage lessons
    def add_lesson(self, lesson):
        """
        Add a lesson to the training if it is not already included.

        Parameters
        ----------
        lesson : any
            The lesson to add.
        """
        if lesson not in self.lessons:
            self.lessons.append(lesson)

    def remove_lesson(self, lesson):
        """
        Remove a lesson from the training if it is present.

        Parameters
        ----------
        lesson : any
            The lesson to remove.
        """
        if lesson in self.lessons:
            self.lessons.remove(lesson)

    def get_lessons(self):
        """
        Return a copy of the lessons list.

        Returns
        -------
        list
            A list of lessons in the training.
        """
        return list(self.lessons)

    def __str__(self):
        """
        Return a human-readable string representation of the training.

        Returns
        -------
        str
            Formatted string with name and dates.
        """
        return (f"Training Name: {self.training_name}, "
                f"Start Date: {self.start_date.strftime('%d/%m/%Y')}, "
                f"End Date: {self.end_date.strftime('%d/%m/%Y')}")


if __name__ == "__main__":
    training = Training(
        "Python Basics",
        date(2024, 7, 1),
        date(2025, 7, 15)
    )
    print(training)
