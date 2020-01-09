export const qS = (arr: number[]) => {
  const _qS = (arr: number[], left: number, right: number) => {
    if (left >= right) {
      return;
    }

    const p = partition2(arr, left, right);

    _qS(arr, left, p - 1);
    _qS(arr, p + 1, right);
  };

  _qS(arr, 0, arr.length - 1);
};

const partition = (arr: number[], begin: number, end: number): number => {
  const pivot = arr[begin];

  while (begin < end) {
    while (begin < end && arr[end] >= pivot) {
      end--;
    }
    arr[begin] = arr[end];
    while (begin < end && arr[begin] <= pivot) {
      begin++;
    }
    arr[end] = arr[begin];
  }
  arr[begin] = pivot;

  return begin;
};

const partition2 = (arr: number[], begin: number, end: number): number => {
  const pivot = arr[begin];
  const index = begin;

  for (let i = index + 1; i <= end; i++) {
    if (arr[i] < pivot) {
      begin++;
      [arr[begin], arr[i]] = [arr[i], arr[begin]];
    }
  }
  [arr[begin], arr[index]] = [arr[index], arr[begin]];

  return begin;
};

const arr: number[] = [5, 5, 21, 1, 2, 24, 6, 2, 13, 1, 3];
qS(arr);
console.info(arr);
