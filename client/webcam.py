import cv2

DEFAULT_PORT = 0

class Webcam:
    """
    Contains general information regarding the webcam agent
    """
    def __init__(self, camera_port = DEFAULT_PORT):
        # Initialize webcam resource:
        self.camera_port = camera_port
        self.capture = cv2.VideoCapture(self.camera_port, cv2.CAP_DSHOW)
        # Change the resolution of the capture:
        # self.capture.set(3,640)
        # self.capture.set(4,480)

        # Check if a video resource is connected:
        if self.capture is None or not self.capture.isOpened():
            raise Exception("Warning: unable to open video source from port: " + str(self.camera_port))

    def dispose_camera(self):
        """
        Dispose the camera resource before shutdown. (Used for testing purposes)
        """
        self.capture.release()

    def capture_frame(self):
        """
        This class function gets a frame from the webcam and returns it.
        """
        return self.capture.read()

    @classmethod
    def image_to_bytes(cls, image) -> bytes:
        """
        This class function converts an image to bytes via the OpenCV library
        """
        return cv2.imencode('.png', image)[1]