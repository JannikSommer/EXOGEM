import os
import cv2
import base64
import numpy as np
from PIL import Image
import face_processing.face_detection as fd
import face_processing.face_recognition as fr

WANTED_FOLDER = os.path.join("resources", "wanted")
THRESHOLD = 0.7

class ProcessImage():
    def __init__(self, wanted_folder_path = WANTED_FOLDER):
        """
        """
        self.recognizer = fr.FaceRecognizer()
        self.detector = fd.FaceDetector()
        
        #Load features from wanted persons:
        self.wanted_features = self._load_wanted_features(wanted_folder_path)

    def _load_wanted_features(self, wanted_folder_path):
        """
        Load features of the wanted people into memory for comparisions
        """
        wanted_features = []
        for filename in os.listdir(wanted_folder_path):
            wanted_features.append((
                filename.replace(".npy", ""),
                np.load(os.path.join(wanted_folder_path, filename))
                ))
        return wanted_features

    def is_wanted(self, image):
        """
        Compares the input image is with the 'wanted' images and determines if any images is recognized. Returns true or false.
        """
        # Detect faces on the image:
        faces = self.detector.get_faces(image)

        # Recognize each face:
        recognized = []
        for face in faces:
            image_face_features = self.recognizer.get_features(self.recognizer.preprocess_image(self.convert_to_PIL(face.face)))
            for name, wanted_face_features in self.wanted_features:
                result = self.recognizer.compare_features(image_face_features, wanted_face_features)
                if result >= THRESHOLD:
                    recognized.append((name, result))
        return recognized
    
    @classmethod
    def convert_to_PIL(cls, image):
        """
        Converts a cv2 image to a PIL image
        """
        im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return Image.fromarray(im)


    @classmethod
    def encode_image(cls, image: bytes) -> str:
        """
        Encode and convert bytes into base64 string.
        """
        s = str(base64.b64encode(image))
        return s[2:len(s)-1]

    @classmethod
    def decode_image(cls, image: str) -> bytes:
        """
        Decode and convert base64 string into bytes.
        """
        return base64.b64decode(image)


if __name__ == "__main__":
    PI = ProcessImage()
    im = cv2.imread("img_8.jpg")
    result = PI.is_wanted(im)
    print("Features extracted")
    for name, acc in result:
        print("ALARM: Recognized " + str(name) + " with accuracy of " + str(acc))
    