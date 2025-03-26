import * as t from "io-ts";
import { decodeAndVerify } from ".";
import { pipe } from "fp-ts/lib/function";
import { fold } from "fp-ts/lib/ReadonlyNonEmptyArray";

/*
### SETUP TYPES
*/
const MakeSchema = t.union([t.literal("Volvo"), t.literal("Other")]);
type Make = t.TypeOf<typeof MakeSchema>;

const CarSchema = t.type({
  make: MakeSchema,
  model: t.string,
});
type Car = t.TypeOf<typeof CarSchema>;

type MakeVolvoType = t.Branded<Car, { readonly Make: unique symbol }>;

const isMakeVolvo = (car: Car): car is MakeVolvoType => car.make === "Volvo";

const MakeVolvoSchema = t.brand(CarSchema, isMakeVolvo, "Make");
type MakeVolvo = t.TypeOf<typeof MakeVolvoSchema>;

/*
### USAGE
*/

export const runSpecificModel = () => {
  const data = {
    volvo: {
      make: "Volvo",
      model: "v60",
    },
    other: {
      make: "Other",
      model: "B-class",
    },
  };

  const validation = MakeVolvoSchema.decode(data.volvo);

  // const resultInValid = decodeAndVerify(
  //   data.other,
  //   MakeVolvoSchema,
  //   "SpecificModel"
  // );
};
