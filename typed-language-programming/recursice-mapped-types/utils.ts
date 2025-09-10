// this function is a helper function to travers the path (given as dot-indextation) inside the Object.
export function getValueAtUsingDotNotation(
  object: Record<string, unknown>,
  path: Array<string>,
  index = 0
): string {
  const key = path[index];
  if (key === undefined) {
    return "";
  }
  const result = object[key];
  if (result === undefined) {
    return "";
  }
  if (typeof result === "string") {
    return result;
  }
  return getValueAtUsingDotNotation(Object(result), path, index + 1);
}
