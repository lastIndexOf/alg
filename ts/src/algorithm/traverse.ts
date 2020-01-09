export const traverseMatrix = (arr: number[][]) => {
  const maxX = arr.length;
  const maxY = arr[0].length;
  const hasTraversed: boolean[][] = [];
  for (let i = 0; i < maxX; i++) {
    hasTraversed[i] = [];
    for (let j = 0; j < maxY; j++) {
      hasTraversed[i][j] = false;
    }
  }

  const results = [];
  let dirc: number = 0;
  let x = 0;
  let y = 0;
  while (true) {
    results.push(arr[x][y]);
    hasTraversed[x][y] = true;
    switch (dirc) {
      case 0:
        if (arr[x][y + 1] && !hasTraversed[x][y + 1]) {
          y++;
          break;
        } else {
          dirc++;
        }
      case 1:
        if (
          Array.isArray(arr[x + 1]) &&
          arr[x + 1][y] &&
          !hasTraversed[x + 1][y]
        ) {
          x++;
          break;
        } else {
          dirc++;
        }
      case 2:
        if (arr[x][y - 1] && !hasTraversed[x][y - 1]) {
          y--;
          break;
        } else {
          dirc++;
        }
      case 3:
        if (
          Array.isArray(arr[x - 1]) &&
          arr[x - 1][y] &&
          !hasTraversed[x - 1][y]
        ) {
          x--;
          break;
        } else {
          dirc = 0;
        }
      default:
        if (arr[x][y + 1] && !hasTraversed[x][y + 1]) {
          y++;
          break;
        } else {
          return results;
        }
    }
  }
};

const arr = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
];
console.info(traverseMatrix(arr));
