class Employee:
    def __init__(self, name, employee_id, total_annual_leave):
        self.name = name  # Public attribute
        self.employee_id = employee_id  # Public attribute
        self._total_annual_leave = total_annual_leave  # Protected attribute
        self._used_annual_leave = 0  # Protected attribute

    def book_leave(self, days):
        """Book a number of days of annual leave for the employee."""
        if days <= 0:
            print(f"{self.name}: Cannot book zero or negative days of leave.")
            return
        if self._used_annual_leave + days <= self._total_annual_leave:
            self._used_annual_leave += days
            print(f"{self.name}: {days} days of leave booked successfully.")
        else:
            available_leave = self._total_annual_leave - self._used_annual_leave
            print(f"{self.name}: Cannot book {days} days of leave. Only {available_leave} days available.")

    def get_remaining_leave(self):
        """Return the remaining annual leave days."""
        return self._total_annual_leave - self._used_annual_leave

    def __str__(self):
        return (f"Employee Name: {self.name}\n"
                f"Employee ID: {self.employee_id}\n"
                f"Total Annual Leave: {self._total_annual_leave}\n"
                f"Used Annual Leave: {self._used_annual_leave}\n"
                f"Remaining Annual Leave: {self.get_remaining_leave()}\n")

def main():
    # Creating an employee object
    emp1 = Employee(name="Ojabo, John Heart", employee_id="E001", total_annual_leave=20)

    # Print employee details
    print(emp1)

    # Booking leave
    emp1.book_leave(5)
    print(emp1)

    emp1.book_leave(10)
    print(emp1)

    emp1.book_leave(10)  # Attempting to book more leave than available
    print(emp1)

    emp1.book_leave(-3)  # Attempting to book negative days of leave
    print(emp1)

if __name__ == '__main__':
    main()
