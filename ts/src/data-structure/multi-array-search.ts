const arr = [
  [1, 2, 8, 9],
  [2, 4, 9, 12],
  [4, 7, 10, 13],
  [6, 8, 11, 15]
];

const func = (arr: number[][], target: number): number[] | null => {
  return calc(arr, 0, arr[0].length - 1, target);
};

const calc = (
  arr: number[][],
  x: number,
  y: number,
  target: number
): number[] | null => {
  if (arr[x][y] === target) {
    return [x, y];
  }

  if (arr[x][y] > target) {
    if (y > 0) {
      return calc(arr, x, y - 1, target);
    } else {
      return null;
    }
  } else {
    if (x < arr.length - 1) {
      return calc(arr, x + 1, y, target);
    } else {
      return null;
    }
  }
};

console.info(func(arr, 17));
