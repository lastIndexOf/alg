export const oddToLeft = (arr: number[]) => {
  const partition = (arr: number[], begin: number, end: number) => {
    const pivot = arr[begin];

    while (begin < end) {
      while (begin < end && arr[end] % 2 === 0) {
        end--;
      }
      arr[begin] = arr[end];
      while (begin < end && arr[begin] % 2 !== 0) {
        begin++;
      }
      arr[end] = arr[begin];
    }
    arr[begin] = pivot;
  };

  partition(arr, 0, arr.length - 1);
};

const arr = [31, 2, 4, 0, 12, 4, 7, 13, 14, 16, 7, 21, 19];
oddToLeft(arr);
console.info(arr);
