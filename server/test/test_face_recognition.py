import unittest
from os import path
from PIL import Image
import face_processing.face_detection as fd
import face_processing.face_recognition as fr


class testFaceRecognition(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #Set-up's the FaceRecognizer for this test file
        self.face_detection = fd.FaceDetector()
        self.face_recognizer = fr.FaceRecognizer()
        
    def test_compare_images_different(self):
        result = self.face_recognizer.compare_images(
            path.join(path.dirname(path.abspath(__file__)), "images", "000001.jpg"), 
            path.join(path.dirname(path.abspath(__file__)), "images", "000002.jpg")
        )
        self.assertLessEqual(result, 0.7) # 0.7 is current recognition threshold

    def test_compare_images_same(self):
        result = self.face_recognizer.compare_images(
            path.join(path.dirname(path.abspath(__file__)), "images", "000001.jpg"), 
            path.join(path.dirname(path.abspath(__file__)), "images", "000001.jpg")
        )
        self.assertGreaterEqual(result, 0.99) 

    def test_cosine_similarity(self):
        f1 = [[1,2,3,4,5,6,7,8,9,10]]
        f2 = [[10,9,8,7,6,5,4,3,2,1]]
        answer = 0.571429
        result = fr.FaceRecognizer.cosine_similarity(f1, f2)
        self.assertAlmostEqual(answer, result, 6)