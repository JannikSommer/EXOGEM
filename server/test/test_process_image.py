import unittest
import wanted_persons
import process_image
from os import path
import os
import cv2
import PIL

WANTED_FOLDER = path.join(path.dirname(path.abspath(__file__)), "wanted")
img1_path = path.join(path.dirname(path.abspath(__file__)), "images", "000001.jpg")
img2_path = path.join(path.dirname(path.abspath(__file__)), "images", "000002.jpg")
img3_path = path.join(path.dirname(path.abspath(__file__)), "images", "000010.jpg")
name1 = "test_person1"
name2 = "test_person2"
class testProcessImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not path.exists(WANTED_FOLDER):
            os.mkdir(WANTED_FOLDER)

    def setUp(self):
        
        self.persons = {}
        wanted_persons.add_person(self.persons, False, name1, img1_path, WANTED_FOLDER)
        wanted_persons.add_person(self.persons, False, name2, img2_path, WANTED_FOLDER)

    def tearDown(self):
        wanted_persons.remove_person(self.persons, False, name1, WANTED_FOLDER)
        wanted_persons.remove_person(self.persons, False, name2, WANTED_FOLDER)

    def test_load_wanted_features(self):
        PI = process_image.ProcessImage(WANTED_FOLDER)
        self.assertEqual(len(PI.wanted_features), 2)

    def test_encode_data(self):
        #Test if data is encoded correctly to base64
        data = "Encode this!"
        
        data_encoded = process_image.ProcessImage.encode_image(bytes(data, "utf-8"))
        self.assertEqual(data_encoded, "RW5jb2RlIHRoaXMh")

    def test_decode_data(self):
        #Test if data is decoded correctly from base64
        data = "RW5jb2RlIHRoaXMh"
        
        data_decoded = process_image.ProcessImage.decode_image(data)
        self.assertEqual(data_decoded, bytes("Encode this!", "utf-8"))

    def test_encode_and_decode_image(self):
        #Tests if 000001.jpg encoded and decoded without dataloss.
        with open(path.join(img1_path), 'rb') as file:
            raw_image = file.read()
            encoded_image = process_image.ProcessImage.encode_image(raw_image)
            decoded_image = process_image.ProcessImage.decode_image(encoded_image)
            
            self.assertEqual(decoded_image, raw_image)

    def test_convert_to_PIL(self):
        image_cv2 = cv2.imread(img1_path)
        image_PIL = process_image.ProcessImage.convert_to_PIL(image_cv2)
        self.assertTrue(isinstance(image_PIL, type(PIL.Image.Image())))

    def test_is_wanted_found(self):
        img = cv2.imread(img1_path)
        PI = process_image.ProcessImage(WANTED_FOLDER)
        results = PI.is_wanted(img)
        self.assertEqual(len(results), 1)
    
    def test_is_wanted_not_found(self):
        img = cv2.imread(img3_path)
        PI = process_image.ProcessImage(WANTED_FOLDER)
        results = PI.is_wanted(img)
        self.assertEqual(len(results), 0)



if __name__ == "__main__":
    unittest.main()