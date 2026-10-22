from product_classification import classify_product

# manual test for checking classification function

examples = [
    ("Food", {"categories_tags": ["en:foods", "en:snacks"]}),
    ("Drink", {"categories_tags": ["en:beverages", "en:waters"]}),
    ("Nonfood", {"categories_tags": ["en:beauty", "en:cosmetics"]}),
    ("Unknown", {"categories_tags": []}),
]

for expected, product in examples:
    result = classify_product(product)
    status = "PASS" if result == expected.upper() else "FAIL"
    print(f"{status}: expected {expected.upper()}, got {result}")
