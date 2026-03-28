from dataclasses import dataclass


@dataclass
class MyExampleData:
    """
    This is a simple dataclass example that contains a string and a dictionary.
    The dataclass decorator automatically generates special methods like __init__() and __repr__() for us.
    """

    data_name: str
    data_dict: dict


def example_1():
    """
    This function demonstrates how to create an instance of the MyExampleData dataclass and print it.
    """
    example_data = MyExampleData(
        data_name="Example Data", data_dict={"key1": "value1", "key2": "value2"}
    )
    print(f"example_data = {example_data}")
    print(
        f"Retrieving data, uses 'dot' notation: 'example_data.data_name' = {example_data.data_name}\n"
        f"'example_data.data_dict' = {example_data.data_dict}\n"
    )
    print(
        "* Since we create the dataclass, without specifying Frozen=True, we can modify the data-instance: 'example_data.data_name = \"New Name\"'"
    )
    example_data.data_name = "New Name"
    print(f"example_data.data_name = {example_data.data_name}")
    print(
        '* Since we create the dataclass, without specifying Frozen=True, we can modify the data_dict: \'example_data.data_dict["key3"] = "value3"\''
    )
    example_data.data_dict["key3"] = "value3"
    print(f"example_data.data_dict = {example_data.data_dict}")


if __name__ == "__main__":
    example_1()
