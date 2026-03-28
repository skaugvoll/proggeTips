from dataclasses import dataclass, field

"""
The most common and "Pythonic" way to add getters and setters is to
use the @property decorator for the getter and @attribute_name.setter for the setter. 
The actual data is usually stored in a "non-public" attribute with a leading underscore (e.g., _attribute). 
"""


@dataclass
class Product:
    # Use a non-public attribute to store the actual value
    # field(init=False) tells dataclass to ignore this field in the generated __init__
    _price: float = field(init=False, repr=False)

    # Public interface for the property
    @property
    def price(self) -> float:
        """The price property getter."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """The price property setter with validation."""
        if value < 0:
            # Better to raise an error than use assert, which can be ignored
            raise ValueError("Price cannot be negative")
        self._price = value


def example_3() -> None:
    """
    This example demonstrates how to use properties in a dataclass to add validation logic for a field.
    We define a Product dataclass with a price field that has a custom setter to ensure the price is not negative.
    """
    # Example Usage:
    item = Product(price=10.99)  # The __init__ uses the setter
    print(item.price)  # Output: 10.99

    item.price = 5.50  # Calls the setter method
    print(item.price)  # Output: 5.50

    try:
        item.price = -1.0
    except ValueError as e:
        print(e)  # Output: Price cannot be negative

    if __name__ == "__main__":
        example_3()
