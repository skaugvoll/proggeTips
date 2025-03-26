import { isRight } from "fp-ts/lib/Either";
import * as t from "io-ts";
import { report } from "io-ts-human-reporter";

interface LegalAgeBrand {
  readonly age: unique symbol;
}
interface IlLegalAgeBrand {
  readonly age: unique symbol;
}

const LegalAgeBrandC = t.brand(
  t.number, // codec
  (n: number): n is t.Branded<number, LegalAgeBrand> => n >= 18 && n <= 100,
  // refinement of the number type
  "age" // name of this codec, must match the unique symbol, must match the unique symbol X in t.Branded<_,X>
);
const IlLegalAgeBrandC = t.brand(
  t.number, // codec
  (n: number): n is t.Branded<number, IlLegalAgeBrand> => n >= 0 && n < 18,
  // refinement of the number type
  "age" // name of this codec, must match the unique symbol X in t.Branded<_,X>
);

type LegalAge = t.TypeOf<typeof LegalAgeBrandC>;
type IlLegalAge = t.TypeOf<typeof IlLegalAgeBrandC>;

const LegalUserC = t.type({
  firstName: t.string,
  lastName: t.string,
  age: LegalAgeBrandC,
});
const IlLegalUserC = t.type({
  firstName: t.string,
  lastName: t.string,
  age: IlLegalAgeBrandC,
});

const UserC = t.union([t.number, LegalUserC, IlLegalUserC]);

const assertLegalAge = (
  user: t.TypeOf<typeof LegalUserC> | t.TypeOf<typeof IlLegalUserC>
): asserts user is t.TypeOf<typeof LegalUserC> => {
  if (!LegalAgeBrandC.is(user.age)) throw new Error("User is not Legal age");
};
const assertIlLegalAge = (
  user: t.TypeOf<typeof LegalUserC> | t.TypeOf<typeof IlLegalUserC>
): asserts user is t.TypeOf<typeof IlLegalUserC> => {
  if (!LegalAgeBrandC.is(user.age)) throw new Error("User is not Legal age");
};

const isLegalAge = (
  user: t.TypeOf<typeof LegalUserC> | t.TypeOf<typeof IlLegalUserC>
): user is t.TypeOf<typeof LegalUserC> => {
  return LegalAgeBrandC.is(user.age);
};
const isIlLegalAge = (
  user: t.TypeOf<typeof LegalUserC> | t.TypeOf<typeof IlLegalUserC>
): user is t.TypeOf<typeof IlLegalUserC> => {
  return IlLegalAgeBrandC.is(user.age);
};

// const decodeAndVerify = (data: t.TypeOf<typeof UserC>) => {
const decodeAndVerify = (data: unknown) => {
  if (isRight(IlLegalUserC.decode(data))) {
    console.log("is under age user");
    return data as t.TypeOf<typeof IlLegalUserC>;
  } else if (isRight(LegalUserC.decode(data))) {
    console.log("is legal age user");
    return data as t.TypeOf<typeof LegalUserC>;
  } else {
    const error =
      report(IlLegalUserC.decode(data)) || report(LegalUserC.decode(data));
    throw new Error(error.join(" "));
  }
};

export const runSpecificModel2 = () => {
  const apiResponseBad = {
    firstName: "a",
    lastName: "b",
    age: 16,
  };
  const apiResponseGood = {
    firstName: "a",
    lastName: "b",
    age: 21,
  };
  try {
    // console.log("AGE : 17");
    // console.log("Legal check: ...");
    // console.log(report(LegalUserC.decode(apiResponseBad)));
    // console.log("Illegal check: ...");
    // console.log(report(IlLegalUserC.decode(apiResponseBad)));
    // console.log("AGE : 21");
    // console.log("Legal check: ...");
    // console.log(report(LegalUserC.decode(apiResponseGood)));
    // console.log("Illegal check: ...");
    // console.log(report(IlLegalUserC.decode(apiResponseGood)));

    const data = decodeAndVerify(apiResponseBad);
    // const data = decodeAndVerify(apiResponseGood);
    console.log("DATA: ", data);
    if (isLegalAge(data)) {
      if (data.age < 10) {
        // would love it if typescript saw the typeguard and understood that this can never happen.
        console.log("this can never happen");
      }
    } else if (isIlLegalAge(data)) {
      if (data.age >= 21) {
        // would love it if typescript saw the typeguard and understood that this can never happen.
        console.log("this can never happen");
      }
    } else {
      console.log("...");
    }
  } catch (e) {
    console.log(`Bad data: ${e}`);
  }
};
