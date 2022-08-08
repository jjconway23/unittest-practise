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

        
    def alert_santa(self):
        self._naughty_list = True

    @property
    def get_email_address(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"