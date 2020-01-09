class Node<T> {
  prev: undefined | Node<T>;
  next: undefined | Node<T>;
  data: T;

  constructor(data: T) {
    this.data = data;
  }
}

const Nodes = [];
class LinkList<T> {
  private _first: undefined | Node<T>;
  private _last: undefined | Node<T>;
  private _size: number = 0;

  get root() {
    return this._first;
  }

  get size() {
    return this._size;
  }

  push(data: T) {
    return this._insert(data, true);
  }

  pop(): T | undefined {
    return;
  }

  unshift(data: T) {
    return this._insert(data, false);
  }

  shift(data: T): T | undefined {
    return;
  }

  reverse() {
    if (!this._first) {
      return;
    }
    return this._reverse(this._first, undefined);
  }

  private _reverse(
    target: Node<T> | undefined,
    next: undefined | Node<T>
  ): any {
    if (!target) {
      return (this._first = next);
    }
    if (!next) {
      this._last = target;
    }
    const oldNext = target.next;
    target.next = next;
    return this._reverse(oldNext, target);
  }

  private _insert(data: T, atEnd: boolean = true) {
    const newNode = new Node<T>(data);
    Nodes.push(newNode);
    if (!this._first) {
      this._first = newNode;
      this._last = newNode;
    } else if (atEnd) {
      const lastNode = this._last;
      lastNode!.next = newNode;
      newNode.prev = lastNode;
      this._last = newNode;
    } else {
      const firstNode = this._first;
      firstNode!.prev = newNode;
      newNode.next = firstNode;
      this._first = newNode;
    }
    this._size += 1;
    return this._remove.bind(this, newNode);
  }

  private _remove() {}
}

export const iter = (arr: number[]): void => {
  _iter1(arr, 0);
};

const _iter1 = (arr: number[], index: number): void => {
  const _task: number[] = [];
  arr.forEach(it => _task.push(it));
  while (_task.length > 0) {
    console.info(_task.pop());
  }
};

const _iter2 = (arr: number[], index: number): void => {
  if (index === arr.length) {
    return;
  }
  _iter2(arr, index + 1);
  console.log(arr[index]);
};

export const deduplicate = (list: LinkList<any>) => {
  let root = list.root ? list.root : undefined;

  while (root) {
    let temp = root.next;
    while (temp) {
      if (temp.data === root.data) {
        temp = temp.next;
      }
    }
    root.next = temp;
    root = temp;
  }
};

export const printReciprocal = (list: LinkList<any>, k: number) => {
  
};

console.info(iter([1, 2, 3, 4, 5, 6]));
