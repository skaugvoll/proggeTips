from dataclasses import dataclass, replace


@dataclass(frozen=True)
class MyExampleFrozenData:
    """
    This is a simple dataclass example that contains a string and a dictionary.
    The dataclass decorator automatically generates special methods like __init__() and __repr__() for us.
    """

    data_name: str
    data_dict: dict


def _sub_example_modify_data_name(example_frozen_data: MyExampleFrozenData) -> None:
    print(
        "* Since we created the dataclass with frozen=True, we cannot modify the instance: "
        "'example_frozen_data.data_name = \"New Name\"'"
    )
    try:
        example_frozen_data.data_name = "New Name"
    except Exception as e:
        print(f"Error: {e} :: {type(e)}")


def _sub_example_replace_data_dict_reference(
    example_frozen_data: MyExampleFrozenData,
) -> None:
    print(
        "* Since we created the dataclass with frozen=True, we cannot reassign the "
        "instance's data_dict reference: "
        '\'example_frozen_data.data_dict = {"new_dict": ""}\''
    )
    try:
        example_frozen_data.data_dict = {"new_dict": ""}
    except Exception as e:
        print(f"Error: {e} :: {type(e)}")


def _sub_example_mutate_data_dict_value(
    example_frozen_data: MyExampleFrozenData,
) -> None:
    print(
        "* Even though the dataclass is frozen=True, we can still mutate values inside "
        "a mutable field like dict:\n"
        '\'example_frozen_data.data_dict["key3"] = "value3"\''
    )
    example_frozen_data.data_dict["key3"] = "value3"
    print(f"example_frozen_data.data_dict = {example_frozen_data.data_dict}")


def _sub_example_replace_data_name_with_replace_function(
    example_frozen_data: MyExampleFrozenData,
) -> None:
    print(
        "* We can use the replace() function from the dataclasses module to create a new instance "
        "with a modified data_name value:\n"
        'new_example_frozen_data = replace(example_frozen_data, data_name="New Name")\n'
        'The "replace" function creates a "clone", only changing the specified field(s) and keeping the rest of the fields the same.'
    )
    new_example_frozen_data = replace(example_frozen_data, data_name="New Name")
    print(f"new_example_frozen_data = {new_example_frozen_data}")


def _sub_example_replace_data_dict_with_replace_function(
    example_frozen_data: MyExampleFrozenData,
) -> None:
    print(
        "* We can use the replace() function from the dataclasses module to create a new instance "
        "with a modified data_dict reference:\n"
        'new_example_frozen_data = replace(example_frozen_data, data_dict={"new_dict": ""})\n'
        'The "replace" function creates a "clone", only changing the specified field(s) and keeping the rest of the fields the same.'
    )
    new_example_frozen_data = replace(example_frozen_data, data_dict={"new_dict": ""})
    print(f"new_example_frozen_data = {new_example_frozen_data}")


def example_2():
    """
    This function demonstrates how to create an instance of the MyExampleFrozenData dataclass and print it.
    """
    example_frozen_data = MyExampleFrozenData(
        data_name="Example Frozen Data",
        data_dict={"key1": "value1", "key2": "value2"},
    )
    print(f"example_frozen_data = {example_frozen_data}")
    print("---")
    _sub_example_modify_data_name(example_frozen_data)
    print("---")
    _sub_example_replace_data_dict_reference(example_frozen_data)
    print("---")
    _sub_example_mutate_data_dict_value(example_frozen_data)
    print("---")
    _sub_example_replace_data_name_with_replace_function(example_frozen_data)
    print("---")
    _sub_example_replace_data_dict_with_replace_function(example_frozen_data)


if __name__ == "__main__":
    example_2()
