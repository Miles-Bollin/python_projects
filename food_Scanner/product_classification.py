"""Classify Open Food Facts products as food, drink, non-food, or unknown."""

FOOD_CATEGORIES = {
	"en:foods",
	"en:food-products",
	"en:plant-based-foods",
	"en:animal-based-foods",
	"en:meals",
	"en:snacks",
	"en:desserts",
	"en:breakfasts",
	"en:dairies",
	"en:fruits",
	"en:vegetables",
	"en:meats",
	"en:fish",
	"en:biscuits-and-cakes",
	"en:chocolates",
	"en:confectioneries",
	"en:bread",
	"en:cereals",
	"en:pastas",
	"en:prepared-foods",
}

DRINK_CATEGORIES = {
	"en:beverages",
	"en:waters",
	"en:soft-drinks",
	"en:juices",
	"en:fruit-juices",
	"en:teas",
	"en:coffees",
	"en:plant-based-beverages",
	"en:milk",
	"en:energy-drinks",
	"en:sports-drinks",
}

NONFOOD_CATEGORIES = {
	"en:non-food-products",
	"en:beauty",
	"en:cosmetics",
	"en:personal-care",
	"en:household-products",
	"en:cleaning-products",
	"en:detergents",
	"en:pet-supplies",
	"en:toys",
	"en:stationery",
	"en:electronics",
	"en:clothing",
}

def classify_product(product):
	"""
	Return FOOD, DRINK, NONFOOD, or UNKNOWN.

	Expects a product dictionary from the Open Food Facst API.
	"""
	if not isinstance(product, dict):
		return "UNKNOWN"

	product_tag = product.get("product_type", "")
	if isinstance(product_tag, str):
		product_tag = product_tag.strip().lower()
	    
	if product_tag == "food":
		return "FOOD"

	categories = product.get("categories_tags",[])

	if not isinstance(categories, list):
		return "UNKNOWN"

	# Clean tag data for easy comparison
	categories = {
		category.strip().lower()
		for category in categories
		if isinstance(category, str)
	}

	if not categories:
		return "UNKNOWN"

	if categories.intersection(DRINK_CATEGORIES):
		return "DRINK"

	if categories.intersection(FOOD_CATEGORIES):
		return "FOOD"

	if categories.intersection(NONFOOD_CATEGORIES):
		return "NONFOOD"

	# default return when categories do not sort properly
	return "UNKNOWN"

def is_accepted_product(product):
	"""Return True only when a product is classified as food or drink."""
	return classify_product(product) in {"FOOD", "DRINK"}

def get_classification_message(product):
	"""Return whether a product is accepted."""
	classification = classify_product(product)

	if classification == "FOOD":
		return "Accepted"
	
	if classification == "DRINK":
		return "Accepted"

	if classification == "NONFOOD":
		return "Rejected: Item is not classified as food"

	return "Rejected: Item could not be verified"
