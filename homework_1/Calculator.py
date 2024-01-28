class Calculator:

    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> int:
        return a // b

    def calculate_discount(self, total: float, discount: float) -> float:
        assert type(discount) in (int, float), f'{discount} should be number'
        assert 0 <= discount <= 100, f'{discount} should be in range [0, 100]'
        return total * (100 - discount) / 100
