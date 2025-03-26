import { getValueAtUsingDotNotation } from "./utils";

/**
 * Stolen from https://gist.github.com/sstur/faa75a1eb04e5b8bcf689bdb4343939b?permalink_comment_id=4604410#gistcomment-4604410
 * for safe keepings and easy access in the future for refrencing.
 */
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
} as const;
// The `as const` insertion is important here for the "bonus".
// Personally, I also think it is good practice to make the locales object read-only
// to avoid accidentally tampering with your app's texts.

type Locales = typeof locales; // entire shape of object locales
type LocaleName = keyof Locales; // the root level keys in object locales
type Locale = Locales[LocaleName]; // the entire shape of first level key in object locales

/**
 * Improves clarity in later type conditionals
 * can be typed directly instead of extracted to Named type (see basic.ts)
 */
type LocaleRecord = { [key: string]: string | LocaleRecord };

/**
 * Make sure we're only using string-type keys
 * can be typed directly instead of extracted to Named type (see basic)
 */
type StringKeysOrNever<T extends object> =
  keyof T extends infer S extends string ? S : never;

/**
 * Improves clarity when defining path keys
 * can be typed directly instead of extracted to Named type (see basic)
 */
type PathKey<First extends string, Tail> = `${First}${Tail extends string
  ? `.${Tail}`
  : never}`;

type PathInto<T extends LocaleRecord> = keyof {
  [K in StringKeysOrNever<T> as T[K] extends string
    ? K
    : // : T[K] extends LocaleRecord
    T[K] extends { [key: string]: string | any }
    ? PathKey<K, PathInto<T[K]>>
    : never]: never; // Use `never` instead of any to prevent the type being used for actual objects
};

/**
 * Cool bonus: Anotates the return value of t() with their actual values !
 * For this to work, you MUST end the definition of {@link locales} with `as const`
 */
type LocaleText<
  Path extends string,
  Locale extends LocaleRecord
> = Path extends `${infer Key}.${infer Tail}`
  ? Locale[Key] extends LocaleRecord
    ? LocaleText<Tail, Locale[Key]>
    : never
  : Locale[Path];

// Here we use type inference to then pass `key`'s literal type to LocaleText
export function t<Key extends PathInto<Locale>>(key: Key) {
  return getValueAtUsingDotNotation(
    locales["en_us"],
    key.split(".")
  ) as LocaleText<Key, Locale>;
  // The `as` assertion here is necessary, since TypeScript can't infer the result of the .split() method.
}

// Place your cursor over this variable and witness the magic of the almighty TypeScript!
const hoverOverMe = {
  1: t("hello"),
  2: t("greetings.morning"),
  3: t("greetings.evening"),
  4: t("greetings.casual.morning"),
  5: t("greetings.casual.afternoon"),
};
/* Hovering over hoverOverMe shows
const hoverOverMe: {
    1: "Hi {user}";
    2: "Good morning {user}";
    3: "Good evening {user}";
    4: "Yo, happy morning";
    5: "Yolo";
}
Notice the actual value's given! this is thankes to using as const!
*/
