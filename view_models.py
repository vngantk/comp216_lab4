
class StudentSurveyViewModel:
    def __init__(self, full_name, residency, program, courses):
        self._full_name = full_name
        self._residency = residency
        self._program = program
        self._courses = courses
        self._listeners = []

    def __str__(self):
        return f"Name: {self.full_name}, Residency: {self.residency}, Program: {self.program}, Courses: {self.courses}"

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    def _fire_change(self, property_name, value):
        for listener in self._listeners:
            listener(self, property_name, value)

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
        self._fire_change("full_name", value)

    @property
    def residency(self):
        return self._residency

    @residency.setter
    def residency(self, value):
        self._residency = value
        self._fire_change("residency", value)

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, value):
        self._program = value
        self._fire_change("program", value)

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, value):
        self._courses = value
        self._fire_change("courses", value)

