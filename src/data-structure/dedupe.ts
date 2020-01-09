const dedupe = (arr: number[]): number[] => {
  // one 哈希表
  const ret: number[] = [];
  const hash: Map<number, any> = new Map();

  arr.forEach((key: number) => {
    if (!hash.has(key)) {
      ret.push(key);
      hash.set(key, true);
    }
  });

  return ret;
  // two: 先排序，再遍历
};

console.info(dedupe([1, 2, 2, 3, 4, 4, 5, 12, 8, 1]));
