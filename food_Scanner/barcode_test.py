def main():
    print("Food & Drink Scanner")
    print("--------------------")

    barcode = input("Enter a barcode: ")

    if barcode == "":
        print("Error: No barcode entered.")
        return

    print()
    print(f"Barcode received: {barcode}")


if __name__ == "__main__":
    main()
