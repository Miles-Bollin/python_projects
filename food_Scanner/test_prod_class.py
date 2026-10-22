import unittest

from product_classification import (
	classify_product,
	is_accepted_product,
	get_classification_message,
)

class TestProdClass(unittest.TestCase):

	def test_food_is_accepted(self):
		product = {"categories_tags": ["en:foods", "en:snacks"]}

		self.assertEqual(classify_product(product), "FOOD")
		self.assertTrue(is_accepted_product(product))
		self.assertIn("Accepted", get_classification_message(product))

	def test_drink_is_accepted(self):
		product = {"categories_tags": ["en:beverages", "en:waters"]}

		self.assertEqual(classify_product(product), "DRINK")
		self.assertTrue(is_accepted_product(product))
		self.assertIn("Accepted", get_classification_message(product))

	def test_nonfood_is_rejected(self):
		product = {"categories_tags": ["en:beauty", "en:cosmetics"]}

		self.assertEqual(classify_product(product), "NONFOOD")
		self.assertFalse(is_accepted_product(product))
		self.assertEqual(
			get_classification_message(product),
			"Rejected: Item is not classified as food"
		)

	def test_unknown_category_is_rejected(self):
		product = {"categories_tags": []}

		self.assertEqual(classify_product(product), "UNKNOWN")
		self.assertFalse(is_accepted_product(product))
		self.assertEqual(
			get_classification_message(product),
			"Rejected: Item could not be verified"
		)

	def test_missing_product_is_rejected(self):
		self.assertEqual(classify_product(None), "UNKNOWN")
		self.assertFalse(is_accepted_product(None))
		self.assertIn("Rejected", get_classification_message(None))

	def test_missing_categories_are_rejected(self):
		product = {"product_name": "Example product"}

		self.assertEqual(classify_product(product), "UNKNOWN")
		self.assertFalse(is_accepted_product(product))
		
	def test_product_type_food_is_accepted(self):
		product = {
			"product_name": "Kraft Macaroni & Cheese Deluxe",
			"product_type": "food",
			"categories_tags": [],
		}

		self.assertEqual(classify_product(product), "FOOD")
		self.assertTrue(is_accepted_product(product))

if __name__ == "__main__":
    unittest.main()
