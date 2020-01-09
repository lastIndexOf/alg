const fibonacciCache: { [key: number]: number } = {};
export const fibonacci = (n: number): number => {
  if (n <= 0) {
    return 0;
  }
  if (n === 1 || n === 2) {
    return 1;
  }
  const result = fibonacciCache[n]
    ? fibonacciCache[n]
    : fibonacci(n - 1) + fibonacci(n - 2);

  fibonacciCache[n] = result;

  return result;
};

export const _fibonacci = (n: number): number => {
  const results: number[] = [];
  let i = 1;
  while (i <= n) {
    if (i === 1) {
      results[i] = 1;
      i++;
      continue;
    }
    if (i === 2) {
      results[i] = 1;
      i++;
      continue;
    }
    results[i] = results[i - 1] + results[i - 2];
    i++;
  }
  return results[n];
};

console.info(fibonacci(120));
console.info(_fibonacci(120));
