# Recursive Mapped Types Terminology

- `extends` must be of type / is of type ...
- `X & Y` all values of X that can / are of type Y ...
- `?` if previous statment is true, then
- `:` if previous statment (before ?) is false, then
- `keyof x` gives key of x
- `typeof x` gives values of x
- `Record<X,Y>` Object where the keys are of type X, and the value of key X is of type Y
- `{ [x]: y }` mapped type
- `{ [z in keyof X]: y}` means for each key z in X, z's value is of type y
- `T[K]` means value of K in object/type T
