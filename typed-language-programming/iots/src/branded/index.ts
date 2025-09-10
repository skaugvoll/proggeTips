import * as t from "io-ts";
import { isLeft } from "fp-ts/lib/Either";
//https://dev.to/derp/bounded-types-in-io-ts-28g5
import { report, reportOne } from "io-ts-human-reporter";

export const decodeAndVerify = <T>(
  data: any,
  type: any,
  usageName: string
): t.Validation<typeof type> | Error => {
  const validity = type.decode(data);
  if (isLeft(validity)) {
    throw Error(
      `Couldn't decode ${usageName} response: ${reportOne(
        validity as t.Validation<typeof type>
      )}`
    );
  }
  return data;
};
