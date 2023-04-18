import unittest
import cv2
import face_processing.face_detection as fd
from os import path

class testFaceDetection(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        #Set-up's the FaceDetector for this test file
        self.face_detection = fd.FaceDetector()

    def test_find_single_faces(self):
        #Test if any faces are detected on 'empty.jpg'.
        image = cv2.imread(path.join(path.dirname(path.abspath(__file__)), "images", "empty.jpg"))
        cropped_faces = self.face_detection.get_faces(image)
        self.assertEqual(len(cropped_faces), 0)

    def test_find_single_faces(self):
        #Test if the face on '000001.jpg' is detected.
        image = cv2.imread(path.join(path.dirname(path.abspath(__file__)), "images", "000001.jpg"))
        cropped_faces = self.face_detection.get_faces(image)
        self.assertEqual(len(cropped_faces), 1)

    def test_find_multiple_faces(self):
        #Test if the faces on 'people.jpg' are detected.
        image = cv2.imread(path.join(path.dirname(path.abspath(__file__)), "images", "people.jpg"))
        cropped_faces = self.face_detection.get_faces(image)
        self.assertEqual(len(cropped_faces), 6)

    def test_face_cropping(self):
        offset = 10
        image = cv2.imread(path.join(path.dirname(path.abspath(__file__)), "images", "000001.jpg"))
        face_no_offset = self.face_detection.get_faces(image, 0)
        face_offset = self.face_detection.get_faces(image, offset)
        height, width, channels = image.shape
        self.assertEqual(face_no_offset[0].width + (2 * offset), face_offset[0].width)
        self.assertEqual(face_no_offset[0].height + (2 * offset), face_offset[0].height)

if __name__ == "__main__":
    unittest.main()