import * as t from "io-ts";
import { decodeAndVerify } from ".";

// Define a type alias for the refined type (a unique brand)
type PositiveNumberType = t.Branded<
  number,
  { readonly PositiveNumber: unique symbol }
>;

// Define a named predicate function using the type alias
const isPositiveNumber = (n: number): n is PositiveNumberType => n > 0;

// Use the `brand` function to create a refined (branded) type named PositiveNumber
// Pass the named predicate function and the type alias to the brand function
const PositiveNumber = t.brand(
  t.number, // Base type: number
  isPositiveNumber, // Named predicate function
  "PositiveNumber" // Identifier for the refinement
);

export const runPositiveNumberExample = () => {
  const data = {
    valid: 42,
    invalid: -24,
  };

  // Usage examples:
  try {
    let errors = {
      valid: null,
      invalid: null,
    };
    // Valid value: 42 (satisfies the constraint)
    errors.valid = decodeAndVerify(
      data.valid,
      PositiveNumber,
      "PositiveNumber"
    );
    // Invalid value: -5 (does not satisfy the constraint)
    // Attempting to use this invalid value will result in a runtime error
    errors.invalid = decodeAndVerify(
      data.invalid,
      PositiveNumber,
      "PositiveNumber"
    );
    console.log(data);
  } catch (e) {
    console.log("Error: ", e);
  }
};
