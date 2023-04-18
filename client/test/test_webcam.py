import cv2
import webcam
import unittest
from os import path
from unittest.case import skipIf

try:
    webcam1 = webcam.Webcam()
except:
    webcam1 = None

class testWebcam(unittest.TestCase):

    @classmethod
    def tearDownClass(self):
        #Disposes the created webcam instantiated in this file when the tests are done
        if webcam1 is not None:
            webcam1.dispose_camera()
            #webcam.dispose()

    @skipIf(webcam1 is None, "No webcam connected")
    def test_webcam(self):
        #Tests if a new Webcam instance is instantiated correctly
        self.assertIsNotNone(webcam1.capture)
        self.assertTrue(webcam1.capture.isOpened())

    @skipIf(webcam1 is None, "No webcam connected")
    def test_take_picture(self):
        successful, picture = webcam1.capture_frame()
        self.assertTrue(successful)
        self.assertIsNotNone(picture)


if __name__ == "__main__":
    unittest.main()