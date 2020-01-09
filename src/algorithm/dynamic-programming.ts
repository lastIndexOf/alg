const cachedValue = new Map<number, number>();
export const splitRope = (n: number): number => {
  if (n <= 4) {
    return n;
  }
  if (cachedValue.has(n)) {
    return cachedValue.get(n)!;
  }
  let max: number = 0;
  for (let i = 1, len = n; i < len; i++) {
    const value = i * splitRope(n - i);
    if (value > max) {
      max = value;
    }
  }
  cachedValue.set(n, max);
  return max;
};

export const splitRope2 = (n: number): number => {
  const caches = [0, 1, 2, 3, 4];
  for (let t = 5; t <= n; t++) {
    let max: number = 0;
    for (let i = 1; i < t; i++) {
      const value = i * caches[t - i];
      if (value > max) {
        max = value;
      }
    }
    caches[t] = max;
  }
  return caches[n];
};

console.info(splitRope(128));
console.info(splitRope2(128));
