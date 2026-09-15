import cv2
import requests

def get_product(barcode):
	url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}"

	headers = {
		"User-Agent": "FoodDrinkScanner/1.0"
	}

	response = requests.get(url, headers=headers, timeout=10)

	if response.status_code != 200:
		print("Error: API request failed.")
		print(f"HTTP status: {response.status_code}")
		print(f"Response: {response.text[:500]}")
		return None

	data = response.json()

	if data.get("status") != 1:
		print("Product not found.")
		return None

	return data["product"]

def display_product(frame, product):
	nutrients = product.get("nutriments", {})

#	variables to display
#    print("\n" + "=" * 40)
#    print("PRODUCT INFORMATION")
#    print("=" * 40)

	product_name = product.get("product_name", "Unknown")
	brand = product.get("brands", "Unknown")

	calories = nutrients.get("energy-kcal_serving", "N/A")
	protein = nutrients.get("proteins_serving", "N/A")
	carbs = nutrients.get("carbohydrates_serving", "N/A")
	fat = nutrients.get("fat_serving", "N/A")
	sugars = nutrients.get("sugars_serving", "N/A")
	fiber = nutrients.get("fiber_serving", "N/A")

	lines = [
		f"Product: {product_name}",
		f"Brand: {brand}",
		f"Calories: {calories} cal",
		f"Protein: {protein} g",
		f"Carbs: {carbs} g",
		f"Fat: {fat} g",
		f"Sugars: {sugars} g",
		f"Fiber: {fiber} g",
	]

	overlay = frame.copy()

	cv2.rectangle(
		overlay,
		(30,30),
		(750, 430),
		(0,0,0),
		-1
	)

	frame = cv2.addWeighted(overlay, 0.75, frame, 0.25, 0)

	y = 70

	for i, line in enumerate(lines):
		if i == 0:
			color = (0, 255, 0)
			scale = 0.9
			thickness = 2
		else:
			color = (255,255,255)
			scale = 0.65
			thickness = 1
		cv2.putText(
			frame,
			line,
			(50, y),
			cv2.FONT_HERSHEY_SIMPLEX,
			scale,
			color,
			thickness,
			cv2.LINE_AA
		)

		y += 38
	return frame

#    print("=" * 40)

def main():
	barcode = input("Scan or enter barcode: ")

	product = get_product(barcode)

	if product is None:
		return

if __name__ == "__main__":
	main()
