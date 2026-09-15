import cv2
from product_api import get_product, display_product

def main():
	camera = cv2.VideoCapture("/dev/video0", cv2.CAP_V4L2)

    # Set camera properties
	camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
	camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
	camera.set(cv2.CAP_PROP_FPS, 30)

    # Display camera properties
	print("Camera width:", camera.get(cv2.CAP_PROP_FRAME_WIDTH))
	print("Camera height:", camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
	print("Camera FPS:", camera.get(cv2.CAP_PROP_FPS))

	if not camera.isOpened():
		print("Error: Could not open camera.")
		return

	print("Camera opened successfully.")
	print("Position a barcode about 6 - 12 inches from the camera.")
	print("Press SPACE to scan.")
	print("Press Q to quit.")

	detector = cv2.barcode.BarcodeDetector()

	product = None

	while True:
		success, frame = camera.read()

		if not success:
			print("Error: Could not read frame.")
			break

		if product is not None:
			frame = display_product(frame, product)

		cv2.imshow("Barcode Scanner", frame)

		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break

        # Spacebar scans the current frame
		if key == ord(" "):

#			cv2.imwrite("barcode_test.jpg", frame)
#			print("\nImage saved as barcode_test.jpg")

			barcode, points, straight_code = (
				detector.detectAndDecode(frame)
			)

			if barcode:
				print(f"Barcode detected: {barcode}")
				print("Looking up product...")

				product = get_product(barcode)

				if product is None:
					print("Could not retrieve product information")
					continue
#				display_product(product)
				print(f"Product: {product.get('product_name', 'Uknown')}")
				print("\nReady for another scan.")

			else:
				print("No barcode detected.")

	camera.release()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
