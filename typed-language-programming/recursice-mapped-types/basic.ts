/**
 * Stolen from https://gist.github.com/sstur/faa75a1eb04e5b8bcf689bdb4343939b
 * for safe keepings and easy access in the future for refrencing.
 */

import { getValueAtUsingDotNotation } from "./utils";

const locales = {
  en_us: {
    hello: "Hi {user}",
    greetings: {
      morning: "Good morning {user}",
      evening: "Good evening {user}",
      casual: {
        morning: "Yo, happy morning",
        afternoon: "Yolo",
      },
    },
  },
};

type Locales = typeof locales; // entire shape of object locales
type LocaleName = keyof Locales; // the root level keys in object locales
type Locale = Locales[LocaleName]; // the entire shape of first level key in object locales

type PathInto<T extends Record<string, any>> = keyof {
  [K in keyof T as T[K] extends string // for each key (K) value in top level of T that are of string
    ? K // if K value is string return K
    : T[K] extends Record<string, any> // if K value is not string, but rather an object
    ? `${K & string}.${PathInto<T[K]> & string}` // if K value is object return K.topKeyLevels under K (this is the recursive part)
    : never]: any; // if K value is not of object (or implicitly string) don't return (not list/ add) // the value of the key we are defining can be any, because we started the type with keyof, meaning disregard the value
};

export function t(key: PathInto<Locale>): string {
  return getValueAtUsingDotNotation(locales[key], key.split("."));
}

const a = t("greetings.casual.afternoon"); // a gets type string instead of value at the path
// const b = t("greetings.goodbye"); // gives error as path (goodbye) is not defined in object
