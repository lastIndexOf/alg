export const translate = (n: number, target: number = 2): number => {
  let result = '';

  while (n !== 0) {
    const item = n % target;
    result += item + '';
    n = (n - item) / target;
  }

  return Number(result);
};

export const translate2 = (n: number): number => {
  let count = 0;
  
  while (n > 0) {
    const result = n & 1;
    if (result === 1) {
      count++;
    }
    n = n >> 1;
  }

  return count;
};

console.info(translate(132131, 2));
console.info(translate2(132131));