export const matchRegExp = (str: string, parten: string): boolean => {
  const strLen = str.length;
  const patLen = parten.length;
  let i = 0;
  let j = 0;

  const _match = (
    str: string,
    len: number,
    index: number,
    parten: string
  ): boolean | number | undefined => {
    while (index < len) {
      if (parten === '.') {
        return i;
      } else if (parten === '*') {
        const i = index;
        while (str[index] === str[i - 1]) {
          index++;
        }
        return index - 1;
      } else {
        return false;
      }
    }
  };

  while (i < strLen) {
    if (str[i] === parten[j]) {
      j++;

      i++;
    } else if (parten[j] === '.' || parten[j] === '*') {
      const result = _match(str, strLen, i, parten[j]);
      if (!result) {
        return false;
      }
      i = (result as number) + 1;
      j++;
    } else {
      return false;
    }
  }

  if (j === patLen) {
    return true;
  }

  return false;
};

console.info(matchRegExp('aaaaab', 'a*b'));
