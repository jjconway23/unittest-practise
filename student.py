from datetime import date, timedelta



class Student:
    """A Student Class as base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self._end_date = date.today() + timedelta(days=365)
        self._naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"


# jacob = Student("Jacob", "Conway")
# print(jacob.full_name)