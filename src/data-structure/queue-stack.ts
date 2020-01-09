export class Queue<T> {
  private head: T[] = [];
  private tail: T[] = [];

  public add(data: T) {
    this.tail.push(data);
  }

  public del(): T | undefined {
    while (this.tail.length) {
      const it = this.tail.pop();
      this.head.push(it!);
    }
    const result = this.head.pop();
    while (this.head.length) {
      const it = this.head.pop();
      this.tail.push(it!);
    }
    return result;
  }
}

const queue = new Queue();
queue.add(1)
queue.add(2)
queue.add(3)
console.info(queue.del());
queue.add(4)
queue.add(5)
console.info(queue.del());
console.info(queue.del());
console.info(queue.del());
console.info(queue.del());
