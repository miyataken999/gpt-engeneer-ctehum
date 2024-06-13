from .models.operation import Operation

class Calculator:
    def __init__(self):
        self.operation = Operation()

    def add(self, num1, num2):
        return self.operation.execute("add", num1, num2)

    def subtract(self, num1, num2):
        return self.operation.execute("subtract", num1, num2)

    def multiply(self, num1, num2):
        return self.operation.execute("multiply", num1, num2)

    def divide(self, num1, num2):
        return self.operation.execute("divide", num1, num2)