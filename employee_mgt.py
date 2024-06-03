from datetime import date

class Employee:
    def __init__(self, name, employee_id, total_annual_leave):
        self.name = name
        self.employee_id = employee_id
        self._total_annual_leave = total_annual_leave
        self._used_annual_leave = 0

    def book_leave(self, days):
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
        return self._total_annual_leave - self._used_annual_leave

    def __str__(self):
        return (f"Employee Name: {self.name}\n"
                f"Employee ID: {self.employee_id}\n"
                f"Total Annual Leave: {self._total_annual_leave}\n"
                f"Used Annual Leave: {self._used_annual_leave}\n"
                f"Remaining Annual Leave: {self.get_remaining_leave()}\n")

class Leave:
    def __init__(self, date, duration):
        self.date = date
        self.duration = duration

    def validate_leave(self):
        # TODO:  Implement validation logic here
        return True

    def apply_leave(self, employee):
        if self.validate_leave():
            employee.book_leave(self.duration)

def main():
    emp1 = Employee(name="Ojabo John Heart", employee_id="E001", total_annual_leave=20)

    print(emp1)

    leave1 = Leave(date=date(2024, 6, 1), duration=5)
    leave1.apply_leave(emp1)
    print(emp1)

    leave2 = Leave(date=date(2024, 6, 15), duration=10)
    leave2.apply_leave(emp1)
    print(emp1)

    leave3 = Leave(date=date(2024, 7, 1), duration=10)
    leave3.apply_leave(emp1)
    print(emp1)

if __name__ == '__main__':
    main()
