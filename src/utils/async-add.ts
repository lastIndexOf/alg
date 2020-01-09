const add = (a: number, b: number): Promise<number> =>
  new Promise(resolve => {
    setTimeout(() => {
      resolve(a + b);
    }, 1e3);
  });

export const asyncAdd = async (numbers: number[]) => {
  const queue: number[] = [];

  const doAdd = async (a: number, b: number): Promise<void> => {
    const result = await add(a, b);

    if (queue.length) {
      const prev = queue.shift();
      return doAdd(result, prev!);
    } else {
      queue.push(result);
    }
    return Promise.resolve();
  };

  const list: Promise<void>[] = [];

  let arg: number | undefined;
  for (const num of numbers) {
    if (arg) {
      list.push(doAdd(arg, num));
      arg = undefined;
    } else {
      arg = num;
    }
  }

  await Promise.all(list);

  return queue[0];
};

const l = new Array<number>(12)
  .fill(0)
  .map(() => Math.round(Math.random() * 20));

console.info('origin: ', l);
console.info(
  'sum: ',
  l.reduce((a, b) => a + b)
);
asyncAdd(l).then(a => console.info(a));
