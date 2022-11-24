export default function cleanSet(set, str) {
    if (!str || !str.length) return '';
    let val = '';
    for (const el of set) {
      if (el && el.startsWith(str)) {
        val += val.length === 0 ? el.replace(str, '') : el.replace(str, '-');
      }
    }
    return val;
  }