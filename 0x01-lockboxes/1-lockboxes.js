function canUnlockAll(boxes) {
  const visitedBoxes = new Set();

  function exploreBox(boxIndex) {
    if (visitedBoxes.has(boxIndex)) {
      return;
    }

    visitedBoxes.add(boxIndex);

    for (const key of boxes[boxIndex]) {
      exploreBox(key);
    }
  }

  exploreBox(0);

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
