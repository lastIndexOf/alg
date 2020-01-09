export const search = (arr: number[], target: number): number => {
  const binarySearch = (
    arr: number[],
    target: number,
    begin: number,
    end: number
  ): number => {
    if (begin + 1 === end) {
      if (arr[begin] === target) {
        return begin;
      }
      if (arr[end] === target) {
        return end;
      }
      return -1;
    }
    const pivot = Math.floor((begin + end) / 2);
    if (arr[pivot] === target) {
      return pivot;
    } else if (arr[pivot] < target) {
      return binarySearch(arr, target, pivot, end);
    } else {
      return binarySearch(arr, target, begin, pivot);
    }
  };

  return binarySearch(arr, target, 0, arr.length - 1);
};

const arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8];
console.info(search(arr, 7));
