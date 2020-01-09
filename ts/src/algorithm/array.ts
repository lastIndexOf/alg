export const fn = (arr: number[], target: number) => {
  return calc(arr, 0, arr.length, target);
};

const calc = (
  arr: number[],
  begin: number,
  end: number,
  target: number
): number[][] => {
  const results: number[][] = [];
  
  for (; begin < end; begin++) {
    const value = arr[begin];
    const rest = target - value;
    if (rest === 0) {
      results.push([value]);
    }
    if (rest > 0) {
      const result = calc(arr, begin + 1, end, rest);
      if (result.length) {
        result.forEach(it => results.push([value, ...it]));
      }
    }
  }

  return results;
};

console.info(fn([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11));
