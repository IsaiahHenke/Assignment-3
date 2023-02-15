import unittest
from datetime import datetime
from student import Student, Assignment, Event

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.event1 = Event("Meeting 1", "meeting", 0)
        self.event2 = Event("Conference 1", "conference", 50)
        self.assignment1 = Assignment("Assignment 1", 80, 100)
        self.assignment2 = Assignment("Assignment 2", 90, 100)
        self.student = Student("John Doe", "12345", "JD", [], [])

    def test_addEvent(self):
        # Test adding single event
        self.student.addEvent(self.event1)
        self.assertEqual(len(self.student.events), 1)
        self.student.addEvent([self.event1, self.event2])
        self.assertEqual(len(self.student.events), 3)

        with self.assertRaises(TypeError):
            self.student.addEvent(123)

    def test_countMeetings(self):
        self.student.addEvent(self.event1)
        self.student.addEvent(self.event2)
        self.student.addEvent(self.event1)
        self.assertEqual(self.student.countMeetings(), 2)

    def test_getGrade(self):
        self.student.addAssignment([self.assignment1, self.assignment2])
        self.assertEqual(self.student.getGrade(), 0.85)

    def test_getLetterGrade(self):
        self.student.addAssignment([self.assignment1, self.assignment2])
        self.assertEqual(self.student.getLetterGrade(0.9), 'A')
        self.assertEqual(self.student.getLetterGrade(0.6), 'D')
        self.assertEqual(self.student.getLetterGrade(), 'B')

    def test_getPercentage(self):
        assignment3 = Assignment("Assignment 3", 50, 75)
        self.assertEqual(assignment3.getPercentage(), 0.6666666666666666)

if __name__ == '__main__':
    unittest.main()