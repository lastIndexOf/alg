class Node {
  next: Node | undefined;
  constructor(public data: number) { }
}
export class Stack {
  private _head: Node | undefined;
  private _min: Node | undefined;

  push(data: number) {
    const old = this._head;
    this._head = new Node(data);
    this._head.next = old;
    if (this._min) {
      this._min = this._min.data > data ? this._head : this._min;
    } else {
      this._min = this._head;
    }
  }

  pop() {
    const data = this._head ? this._head.data : undefined;
    if (this._head) {
      this._head = this._head.next;
    }
    return data;
  }

  min() {
    if (this._min) {
      return this._min.data;
    }
  }
}

export class Stack2 {
  private stack: number[] = [];
  private _auxiliary: number[] = [];
  private _min: number | undefined;

  push(data: number) {
    if (this._min) {
      this._min = this._min > data ? data : this._min;
    } else {
      this._min = data;
    }
    this._auxiliary.push(this._min);
  }

  pop() {
    this._auxiliary.pop();
    this._min = this._auxiliary.pop();
    if (this._min) this._auxiliary.push(this._min);
    return this.stack.pop();
  }

  min() {
    return this._min;
  }
}

const arr = new Stack2();

arr.push(10);
arr.push(14);
arr.push(9);
arr.push(4);

const initial = [1, 2, 3, 4, 5];
const order = [4, 5, 3, 2, 1];

export const judge = (initial: number[], order: number[]): boolean => {
  const stack: number[] = [];

  let orderIndex = 0;
  for (let i = 0, len = initial.length; i < len; i++) {
    if (initial[i] !== order[orderIndex]) {
      stack.push(initial[i]);
    } else {
      orderIndex++;
      while (true) {
        const value = stack.pop();
        if (order[orderIndex] && value === order[orderIndex]) {
          orderIndex++;
          continue;
        }
        if (value) {
          stack.push(value);
        }
        break;
      }
    }
  }

  while (stack.length) {
    const pop = stack.pop();
    if (pop !== order[orderIndex]) {
      return false;
    }
    orderIndex++;
  }

  return true;
};

console.log(judge(initial, order));
