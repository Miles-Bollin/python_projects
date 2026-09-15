import cv2

def main():
    camera = cv2.VideoCapture("/dev/video0")	#open camera

    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    print("Camera opened successfully.")
    print("Press Q to quit.")

    while True:
        success, frame = camera.read()	# constant update of the current camera frame

        if not success:
            print("Error: Could not read frame.")
            break

        print(frame.shape)	#display frame data (height, width, color channels)

        cv2.imshow("Food & Drink Scanner - Camera Test", frame)	# Displays latest frame

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()	# stop using camera for this application
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
