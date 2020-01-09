const shuffle = (arr: number[]): number[] => {
  const ret = [...arr];
  const len = ret.length;
  let index = len - 1;
  while (index > 0) {
    const ranIndex = Math.floor(Math.random() * index);
    [ret[index], ret[ranIndex]] = [ret[ranIndex], ret[index]];
    index--;
  }
  return ret;
};

console.info(shuffle([1, 2, 3, 4, 5, 6]));
