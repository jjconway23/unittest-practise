import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student("John", "Doe")

        self.assertEqual(student.full_name, "John Doe")

    def test_alert_santa(self):
        student = Student("John", "Doe")
        student.alert_santa()

        self.assertTrue(student._naughty_list)


    def test_get_email_address(self):
        student = Student("John", "Doe")
        self.assertEqual(student.get_email_address, "john.doe@email.com")




if __name__ == "__main__":
    unittest.main()
