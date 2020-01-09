class Node<T> {
  left: Node<T> | undefined;
  right: Node<T> | undefined;
  data: T;

  constructor(data: T) {
    this.data = data;
  }
}

class BinaryTree<T> {
  root: Node<T> | undefined;
}

const frontTravel = [1, 2, 4, 7, 3, 5, 6, 8];
const middleTravel = [4, 7, 2, 1, 5, 3, 8, 6];

export const reBuildBinaryTreeByFrontTravelAndMiddleTravel = (
  tree: BinaryTree<number>,
  front: number[],
  middle: number[]
) => {
  const root = front[0];
  const rootIndexInMiddle = middle.findIndex(it => it === root);
  tree.root = new Node(root);
  const left = middle.slice(0, rootIndexInMiddle);
  const right = middle.slice(rootIndexInMiddle + 1, middle.length);
  travel(tree.root, left, right, front);
};

const travel = (
  root: Node<number>,
  left: number[],
  right: number[],
  target: number[]
) => {
  if (left.length) {
    const leftIndex = calcNodeIndex(left, target);
    root.left = new Node(left[leftIndex!]);
    travel(
      root.left,
      left.slice(0, leftIndex),
      left.slice(leftIndex! + 1, left.length),
      target
    );
  }
  if (right.length) {
    const rightIndex = calcNodeIndex(right, target);
    root.right = new Node(right[rightIndex!]);
    travel(
      root.right,
      right.slice(0, rightIndex),
      right.slice(rightIndex! + 1, right.length),
      target
    );
  }
};

const calcNodeIndex = (
  queue: number[],
  target: number[]
): number | undefined => {
  for (let i = 0, len = target.length; i < len; i++) {
    const index = queue.findIndex(it => it === target[i]);
    if (index > -1) {
      return index;
    }
  }
};

const tree = new BinaryTree<number>();

reBuildBinaryTreeByFrontTravelAndMiddleTravel(tree, frontTravel, middleTravel);

(() => {
  const aQueue: number[] = [];
  const a = (root: Node<number> | undefined) => {
    if (root) {
      aQueue.push(root.data);
      a(root.left);
      a(root.right);
    }
  };
  const _a = (tree: BinaryTree<number>) => {
    let root = tree.root;
    if (!root) {
      return;
    }
    const _queue: Node<number>[] = [root];
    while (_queue.length || root) {
      console.info(root!.data);

      if (root!.left) {
        root = root!.left;
      }
    }
  };
  const bQueue: number[] = [];
  const b = (root: Node<number> | undefined) => {
    if (root) {
      b(root.left);
      bQueue.push(root.data);
      b(root.right);
    }
  };

  a(tree.root);
  b(tree.root);
  console.info(aQueue.join(' '));
  console.info(bQueue.join(' '));
})();

// second
export const calcNextNodeByMiddle = (
  tree: BinaryTree<number>,
  data: number
): number | undefined => {
  let temp: number[] = [];
  let result: number | undefined;
  const MS = (root: Node<number>, atNode: boolean = false) => {
    if (root.left) {
      MS(root.left);
    }
    const it = temp.pop();
    if (it === data) {
      result = root.data;
    } else {
      temp.push(root.data);
    }
    if (root.right) {
      MS(root.right);
    }
  };
  MS(tree.root!);
  return result;
};

export const wfs = (tree: BinaryTree<number>) => {
  const queue: Node<number>[] = [];
  const results: any[] = [];
  let pointer: number = 1;
  const _wfs = () => {
    if (queue.length) {
      const node = queue.shift();
      pointer--;
      results.push(node!.data);
      if (node!.left) {
        queue.push(node!.left);
        pointer++;
      }
      if (node!.right) {
        queue.push(node!.right);
        pointer++;
      }
      if (pointer === 0) {
        results.push('\n');
      }
      _wfs();
    }
  };
  if (tree.root) {
    queue.push(tree.root);
    _wfs();
  }
  console.info(results.join(' '));
};

export const include = (
  tree: Node<any> | undefined,
  child: Node<any> | undefined
): boolean => {
  if (!tree) {
    return false;
  }
  if (!child) {
    return true;
  }

  let result = false;
  if (tree.data === child.data) {
    result =
      hasSubTree(tree.left, child.left) && hasSubTree(tree.right, child.right);
    if (result) return true;
  }

  return include(tree.left, child) || include(tree.right, child);
};

const hasSubTree = (
  tree: Node<any> | undefined,
  child: Node<any> | undefined
): boolean => {
  if (!child) {
    return true;
  }
  if (!tree) {
    return false;
  }
  if (tree!.data === child!.data) {
    return (
      hasSubTree(tree!.left, child!.left) &&
      hasSubTree(tree!.right, child!.right)
    );
  }
  return false;
};

export const reverse = (tree: BinaryTree<number>): BinaryTree<number> => {
  const newTree = new BinaryTree<number>();

  if (tree.root) {
    newTree.root = new Node(tree.root.data);
    doReverse(tree.root, newTree.root);
  }

  return newTree;
};
const doReverse = (oldNode: Node<number>, newNode: Node<number>) => {
  if (oldNode.right) {
    newNode.left = new Node(oldNode.right.data);
    doReverse(oldNode.right, newNode.left);
  }
  if (oldNode.left) {
    newNode.right = new Node(oldNode.left.data);
    doReverse(oldNode.left, newNode.right);
  }
};

export const isEqualWithMirror = (tree: BinaryTree<number>) => {
  if (!tree.root) {
    return true;
  }
  if (tree.root.left && tree.root.right) {
    return isMirror(tree.root.left, tree.root.right);
  }
  return false;
};
const isMirror = (left: Node<number>, right: Node<number>): boolean => {
  if (left.data !== right.data) {
    return false;
  }
  let result = false;
  if (left.left && right.right) {
    result = isMirror(left.left, right.right);
  }
  if (left.right && right.left) {
    result = isMirror(left.right, right.left);
  }
  if (!left.left && !right.right && !left.right && !right.left) {
    result = true;
  }
  return result;
};

const child = new BinaryTree<number>();
child.root = new Node(1);
child.root.left = new Node(4);
child.root.left.left = new Node(6);
child.root.right = new Node(4);
child.root.right.right = new Node(6);

export const wfsf = (tree: BinaryTree<number>) => {
  if (!tree.root) {
    return;
  }
  const results: number[] = [];
  const print = (nodes: Node<number>[]) => {
    const newNodes: Node<number>[] = [];
    if (!nodes.length) {
      return;
    }
    nodes.forEach(node => {
      results.push(node.data);
      if (node.left) {
        newNodes.push(node.left);
      }
      if (node.right) {
        newNodes.push(node.right);
      }
    });
    results.push('\n' as any);
    print(newNodes);
  };
  print([tree.root]);
  results[0] = (' ' + results[0]) as any;
  console.info(results.join(' '));
};

wfs(tree);

const searchArr = [5, 7, 6, 9, 11, 10, 8];
const errorSearchArr = [7, 4, 6, 5];

export const isSearchBinaryTreeByEFS = (arr: number[]): boolean => {
  if (!arr.length) {
    return true;
  }
  return _judgeSBT(arr, 0, arr.length - 1);
};

const _judgeSBT = (arr: number[], begin: number, end: number): boolean => {
  if (begin === end) {
    return true;
  }
  const root = arr[end];

  let rightBegin = begin;
  while (arr[rightBegin] < root && rightBegin < end) {
    rightBegin++;
  }
  const leftEnd = rightBegin - 1;
  if (rightBegin === end) {
    return _judgeSBT(arr, begin, leftEnd);
  }

  let index = rightBegin;
  while (index < end) {
    if (arr[index] < root) {
      return false;
    }
    index++;
  }
  if (rightBegin === begin) {
    return _judgeSBT(arr, begin, end - 1);
  }

  return _judgeSBT(arr, begin, leftEnd) && _judgeSBT(arr, rightBegin, end - 1);
};

console.info(isSearchBinaryTreeByEFS(searchArr));
console.info(isSearchBinaryTreeByEFS(errorSearchArr));
