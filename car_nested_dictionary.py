class Car:
    def __init__(self):
        # Nested dictionary containing car data
        self.cars = {
            "Sedan": {
                "Toyota Camry": {"year": 2020, "price": 24000},
                "Honda Accord": {"year": 2021, "price": 26000},
            },
            "SUV": {
                "Toyota RAV4": {"year": 2019, "price": 28000},
                "Honda CR-V": {"year": 2022, "price": 30000},
            },
            "Truck": {
                "Ford F-150": {"year": 2018, "price": 35000},
                "Chevrolet Silverado": {"year": 2020, "price": 37000},
            }
        }

    def get_items(self):
        """Returns the items of the cars dictionary."""
        return self.cars.items()

    def get_keys(self):
        """Returns the keys of the cars dictionary."""
        return self.cars.keys()

    def get_values(self):
        """Returns the values of the cars dictionary."""
        return self.cars.values()


def main():
    car_inventory = Car()

    # Print items of the cars dictionary
    print("Items in the car inventory:")
    for category, models in car_inventory.get_items():
        print(f"{category}:")
        for model, details in models.items():
            print(f"  {model}: {details}")

    # Print keys of the cars dictionary
    print("\nCategories in the car inventory:")
    for key in car_inventory.get_keys():
        print(key)

    # Print values of the cars dictionary
    print("\nDetails of all cars in the inventory:")
    for value in car_inventory.get_values():
        print(value)


if __name__ == "__main__":
    main()
