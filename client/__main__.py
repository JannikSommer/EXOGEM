import time
import argparse
import webcam as cam
from datetime import timedelta, datetime
from process_node_interface import ProcessNodeInterface
from openapi_client.model.monitor_data import MonitorData


DEFAULT_INTERVAL = 1000

def main(location: str, interval: int = DEFAULT_INTERVAL) -> None:

    # Initialize components:
    pni = ProcessNodeInterface()
    try:
        # Instantiate the webcam class, it can raise an exception if there is no webcam connected to the host 
        webcam = cam.Webcam()
    except Exception as e:
        print(e)
        exit()

    # Setup local variables:
    image_num = 0
    prev_time = datetime.now()

    print("Capturing images every " + str(interval) + " milliseconds at " + location + "\nPress CTRL-C to terminate program.")
    try:
        while True:
            # Continue if the correct time has elapsed since 'prev_time' which is update at the end of each iteration of the while loop.
            if prev_time + timedelta(milliseconds=interval) <= datetime.now():
                # Load a frame from the connected webcam:
                successful, image = webcam.capture_frame()
                if successful == True:
                    # Send image processing request to server
                    pni.process_image(
                        image_data = pni.encode_image(webcam.image_to_bytes(image)),
                        location = location,
                        monitor_data = MonitorData(request_id = str(image_num))
                    )
                    image_num += 1
                prev_time = datetime.now()
            else:
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program terminated")
        exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interval", type=int, default=DEFAULT_INTERVAL, metavar="ms", help="Milliseconds between each image processing request")
    parser.add_argument("location", type=str, help="Physical location of the camera")
    args = parser.parse_args()
    main(args.location, args.interval)