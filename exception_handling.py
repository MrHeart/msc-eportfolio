def perform_operations():
    try:
        # Attempting to divide by zero
        result = 10 / 0
        print(result)

    except ValueError:
        # Handle ValueError exception
        print("A ValueError occurred.")

    except (TypeError, ZeroDivisionError) as e:
        # Handle multiple exceptions: TypeError and ZeroDivisionError
        print(f"An error occurred: {e}")

    except Exception as e:
        # Handle all other exceptions
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    perform_operations()
