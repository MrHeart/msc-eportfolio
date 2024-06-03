class MyClass:
    def __init__(self):
        # Unprotected variable
        self.unprotected_var = "I am unprotected"

        # Protected variable (using single underscore convention)
        self._protected_var = "I am protected"

    def display(self):
        print("Unprotected variable:", self.unprotected_var)
        print("Protected variable:", self._protected_var)


# Instantiate the class
obj = MyClass()

# Accessing and displaying variables
print("Accessing variables directly:")
print("Unprotected variable:", obj.unprotected_var)
print("Protected variable:", obj._protected_var)

print("\nAccessing variables using method:")
obj.display()
