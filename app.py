
def add_numbers(a, b):
    return a + b


def greet_user(name):
    return f"Hello, {name}!"


def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    return price - (price * discount_percent / 100)


if __name__ == "__main__":
    print("Dummy CI/CD Application Started")

    print("Addition:", add_numbers(10, 20))
    print(greet_user("Urvish"))
    print("Discounted price:", calculate_discount(1000, 10))
