import os
import unittest
import wanted_persons
from os import path

IMG_PATH = path.join(path.dirname(path.abspath(__file__)), "images", "000001.jpg")
WANTED_FOLDER = path.join(path.dirname(path.abspath(__file__)), "wanted")

class testWantedPersons(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not path.exists(WANTED_FOLDER):
            os.mkdir(WANTED_FOLDER)

    def test_add_person(self):
        name = "test_person"
        persons = {} # dict of person names
        wanted_persons.add_person(persons, False, name, IMG_PATH, WANTED_FOLDER)
        self.assertTrue(name in persons)
        self.assertTrue(path.exists(path.join(WANTED_FOLDER, name + ".npy")))
        if path.exists(path.join(WANTED_FOLDER, name + ".npy")):
            os.remove(path.join(WANTED_FOLDER, name + ".npy"))

    def test_remove_person(self):
        name = "test_person"
        persons = {} # dict of person names
        wanted_persons.add_person(persons, False, name, IMG_PATH, WANTED_FOLDER)
        self.assertTrue(path.exists(path.join(WANTED_FOLDER, name + ".npy")))
        wanted_persons.remove_person(persons, False, name, WANTED_FOLDER)
        self.assertFalse(name in persons)
        self.assertFalse(path.exists(path.join(WANTED_FOLDER, name + ".npy")))

        
if __name__ == "__main__":
    unittest.main()