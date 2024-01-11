function canUnlockAll(boxes) {
  const visitedBoxes = new Set();
  const queue = [0]; // Start with the first box

  while (queue.length > 0) {
    const currentBox = queue.shift();

    if (!visitedBoxes.has(currentBox)) {
      visitedBoxes.add(currentBox);

      for (const key of boxes[currentBox]) {
        queue.push(key);
      }
    }
  }

  return visitedBoxes.size === boxes.length;
}

const boxes1 = [
  [1],
  [2],
  [],
  [0],
];

console.log(canUnlockAll(boxes1)); // Expected output: true

const boxes2 = [
  [1, 2],
  [3],
  [],
  [0],
];

console.log(canUnlockAll(boxes2)); // Expected output: false
