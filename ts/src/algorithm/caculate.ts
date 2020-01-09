export const Power = (base: number, exponent: number): number => {
  if (exponent === 0) {
    return 1;
  }

  const isPositive = exponent > 0;
  exponent = isPositive ? exponent : -exponent;

  let sum: number = 1;
  while (exponent > 0) {
    exponent--;
    sum *= base;
  }

  return isPositive ? sum : sum === 0 ? 0 : 1 / sum;
};

export const printMaxNBaseNumber = (n: number): number[] => {
  if (n <= 0) {
    return [];
  }

  let sum = 9;
  while (n - 1 > 0) {
    n--;
    sum = 10 * sum + 9;
  }

  const results: number[] = [];
  for (let i = 1; i <= sum; i++) {
    results.push(i);
  }

  return results;
};

console.info(Power(2, -2));
console.info(printMaxNBaseNumber(3).length);
