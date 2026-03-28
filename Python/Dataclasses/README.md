# Python Dataclasses

Python dataclasses provide a decorator and functions for automatically generating special methods in classes primarily designed to store data. This saves developers from writing repetitive boilerplate code like `__init__()`, `__repr__()`, and `__eq__()`

Dataclasses are created by decorating a regular class with the decorator `@dataclass`

```python
import dataclasses
@dataclass
class MyData():
  var1: str
```

- Dataclasses are optimized for use as data containers (like "mutable namedtuples with defaults"), making them ideal when the main purpose of a class is to store attributes.
- Decorator: They are created by decorating a regular class with @dataclass.
- Type Hints: Field definitions require type annotations (type hints), which the decorator inspects to generate the necessary methods. These hints are not enforced at runtime by default.

## Dataclass decorator arguments

See [docs](https://docs.python.org/3/library/dataclasses.html#module-contents) for more in-depth

```python
@dataclasses.dataclass(
  *,
  init=True,
  repr=True,
  eq=True,
  order=False,
  unsafe_hash=False,
  frozen=False,
  match_args=True,
  kw_only=False,
  slots=False,
  weakref_slot=False
)
```

### Argument meaning

The parameters to @dataclass are:

- `init`: If true (the default), a **init**() method will be generated.

  If the class already defines **init**(), this parameter is ignored.

- `repr`: If true (the default), a **repr**() method will be generated. The generated repr string will have the class name and the name and repr of each field, in the order they are defined in the class. Fields that are marked as being excluded from the repr are not included. For example: InventoryItem(name='widget', unit_price=3.0, quantity_on_hand=10).

  If the class already defines **repr**(), this parameter is ignored.

- `eq`: If true (the default), an **eq**() method will be generated. This method compares the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type.

  If the class already defines **eq**(), this parameter is ignored.

- `order`: If true (the default is False), **lt**(), **le**(), **gt**(), and **ge**() methods will be generated. These compare the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type. If order is true and eq is false, a ValueError is raised.

  If the class already defines any of **lt**(), **le**(), **gt**(), or **ge**(), then TypeError is raised.

- `unsafe_hash`: If true, force dataclasses to create a **hash**() method, even though it may not be safe to do so. Otherwise, generate a **hash**() method according to how eq and frozen are set. The default value is False.

  **hash**() is used by built-in hash(), and when objects are added to hashed collections such as dictionaries and sets. Having a **hash**() implies that instances of the class are immutable. Mutability is a complicated property that depends on the programmer’s intent, the existence and behavior of **eq**(), and the values of the eq and frozen flags in the @dataclass decorator.

  By default, @dataclass will not implicitly add a **hash**() method unless it is safe to do so. Neither will it add or change an existing explicitly defined **hash**() method. Setting the class attribute **hash** = None has a specific meaning to Python, as described in the **hash**() documentation.

  If **hash**() is not explicitly defined, or if it is set to None, then @dataclass may add an implicit **hash**() method. Although not recommended, you can force @dataclass to create a **hash**() method with unsafe_hash=True. This might be the case if your class is logically immutable but can still be mutated. This is a specialized use case and should be considered carefully.

  Here are the rules governing implicit creation of a **hash**() method. Note that you cannot both have an explicit **hash**() method in your dataclass and set unsafe_hash=True; this will result in a TypeError.

  If `eq` and `frozen` are both true, by default @dataclass will generate a **hash**() method for you. If eq is true and frozen is false, **hash**() will be set to None, marking it unhashable (which it is, since it is mutable). If eq is false, **hash**() will be left untouched meaning the **hash**() method of the superclass will be used (if the superclass is object, this means it will fall back to id-based hashing).

- `frozen`: If true (the default is False), assigning to fields will generate an exception. This emulates read-only frozen instances. See the discussion below.

  If **setattr**() or **delattr**() is defined in the class and frozen is true, then TypeError is raised.

- `match_args`: If true (the default is True), the **match_args** tuple will be created from the list of non keyword-only parameters to the generated **init**() method (even if **init**() is not generated, see above). If false, or if **match_args** is already defined in the class, then **match_args** will not be generated.

  > Added in version 3.10.

- `kw_only`: If true (the default value is False), then all fields will be marked as keyword-only. If a field is marked as keyword-only, then the only effect is that the **init**() parameter generated from a keyword-only field must be specified with a keyword when **init**() is called. See the parameter glossary entry for details. Also see the KW_ONLY section.

  Keyword-only fields are not included in **match_args**.

  > Added in version 3.10.

- `slots`: If true (the default is False), **slots** attribute will be generated and new class will be returned instead of the original one. If **slots** is already defined in the class, then TypeError is raised.

  Warning Passing parameters to a base class **init_subclass**() when using slots=True will result in a TypeError. Either use **init_subclass** with no parameters or use default values as a workaround. See gh-91126 for full details.
  Added in version 3.10.

  Changed in version 3.11: If a field name is already included in the **slots** of a base class, it will not be included in the generated **slots** to prevent overriding them. Therefore, do not use **slots** to retrieve the field names of a dataclass. Use fields() instead. To be able to determine inherited slots, base class **slots** may be any iterable, but not an iterator.

- `weakref_slot`: If true (the default is False), add a slot named “**weakref**”, which is required to make an instance weakref-able. It is an error to specify weakref_slot=True without also specifying slots=True.

  > Added in version 3.11.
