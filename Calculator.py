class Calculator:
    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero!"
    
    def power(self, a, b):
        return a ** b

def main():
    cal = Calculator()
    while True:
        print("=" * 50)
        print("CALCULATOR APP")
        print("=" * 50)
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. power")
        print("6. Exit")
        print("=" * 50)
        
        try:
            choice = int(input("Enter your choice (1/2/3/4/5/6): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1-6.")
            continue
        
        if choice not in range(1,7):
            print("Invalid choice! Please enter a number between 1-6.")
            continue
            
        if choice == 6:
            print("Thank you for using the calculator system!")
            break
        
        
        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))
        
        if choice == 1:
            result = cal.addition(a, b)
            print(f"Result: {a} + {b} = {result}")
        elif choice == 2:
            result = cal.subtraction(a, b)
            print(f"Result: {a} - {b} = {result}")
        elif choice == 3:
            result = cal.multiplication(a, b)
            print(f"Result: {a} × {b} = {result}")
        elif choice == 4:
            result = cal.division(a, b)
            print(f"Result: {a} ÷ {b} = {result}")
        elif choice == 5:
            result = cal.power(a, b)
            print(f"Result: {a} ^ {b} = {result}")
        
main()