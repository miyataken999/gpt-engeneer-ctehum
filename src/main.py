from .calculator import Calculator

def main():
    calculator = Calculator()
    result = calculator.add(2, 3)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()