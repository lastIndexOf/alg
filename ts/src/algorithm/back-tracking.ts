export const backTracking = (arr: string[][], route: string) => {
  const routes = route.split('');

  const maxX = arr.length;
  const maxY = arr[0].length;

  for (let x = 0; x < maxX; x++) {
    for (let y = 0; y < maxY; y++) {
      const though = [
        [false, false, false, false],
        [false, false, false, false],
        [false, false, false, false]
      ];
      const stack: number[][] = [];
      const point = getStartPoint(arr, x, y, routes[0], though, stack);
      if (point) {
        if (checkPoint(arr, point[0], point[1], routes)) {
          return true;
        }
      }
    }
  }
};

const getStartPoint = (
  arr: string[][],
  x: number,
  y: number,
  value: string,
  through: boolean[][],
  stack: number[][]
): number[] | undefined => {
  if (arr[x][y] === value) {
    return [x, y];
  }
  stack.push([x, y]);
  through[x][y] = true;
  if (arr[x - 1]) {
    if (!through[x - 1][y])
      return getStartPoint(arr, x - 1, y, value, through, stack);
  }
  if (arr[x + 1]) {
    if (!through[x + 1][y])
      return getStartPoint(arr, x + 1, y, value, through, stack);
  }
  if (arr[x][y - 1]) {
    if (!through[x][y - 1])
      return getStartPoint(arr, x, y - 1, value, through, stack);
  }
  if (arr[x][y + 1]) {
    if (!through[x][y + 1])
      return getStartPoint(arr, x, y + 1, value, through, stack);
  }
  stack.pop();
};

const checkPoint = (
  arr: string[][],
  x: number,
  y: number,
  routes: string[]
): boolean => {
  const _check = (arr: string[][], x: number, y: number, value: string) => {
    if (arr[x - 1]) {
      return arr[x - 1][y] === value ? [x - 1, y] : false;
    }
    if (arr[x + 1]) {
      return arr[x + 1][y] === value ? [x + 1, y] : false;
    }
    if (arr[x][y - 1]) {
      return arr[x][y - 1] === value ? [x, y - 1] : false;
    }
    if (arr[x][y + 1]) {
      return arr[x][y + 1] === value ? [x, y + 1] : false;
    }
  };
  for (let i = 1, len = routes.length; i < len; i++) {
    const flag = _check(arr, x, y, routes[i]);
    if (!flag) {
      return false;
    } else {
      [x, y] = flag;
    }
  }
  return true;
};

const arr = [
  ['a', 'b', 't', 'g'],
  ['c', 'f', 'c', 's'],
  ['j', 'd', 'e', 'h']
];

console.info(backTracking(arr, 'cfba'));

// TODO arr[x][y]
// TODO 上 arr[x - 1][y]
// TODO 下 arr[x + 1][y]
// TODO 左 arr[x][y - 1]
// TODO 右 arr[x][y + 1]
