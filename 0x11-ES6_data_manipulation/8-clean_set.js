export default function cleanSet(set, startString) {
  const string = [];

  if (typeof startString !== 'string' || typeof set !== 'object' || startString.length === 0) {
    return '';
  }

  for (const item of set) {
    if (item && item.startsWith(startString)) {
      string.push(item.slice(startString.length));
    }
  }

  return string.join('-');
}
