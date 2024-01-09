# Algorithm Challenge: Lockboxes

## Problem Description

You are given a set of lockboxes, each with a unique positive integer key. The keys are represented as an array of arrays, where each inner array contains the keys of a single lockbox. Additionally, some lockboxes contain keys to other lockboxes.

Your goal is to determine if it's possible to open all lockboxes by recursively following the keys. You start with the first box, and if it contains keys, you may choose any of those keys to open another box. The process continues until all boxes are open or no more boxes can be opened.

Write a function `canUnlockAll(boxes)` that takes in an array of lockboxes and returns a boolean indicating whether all boxes can be opened.

### Example

```javascript
const boxes = [
  [1],        // Box 0 has a key to Box 1
  [2],        // Box 1 has a key to Box 2
  [],         // Box 2 has no keys
  [0],        // Box 3 has a key to Box 0
];

console.log(canUnlockAll(boxes));  // Output: true
```

## Implementation Details

### Function Signature

```javascript
function canUnlockAll(boxes) {
  // Implementation goes here
}
```

### Approach

We can solve this problem by using depth-first search (DFS) or breadth-first search (BFS). The idea is to keep track of the boxes that we have already opened and explore the keys in a recursive manner. If, during the exploration, we encounter a key to a box that we haven't opened yet, we recursively open that box and continue the process.

### Pseudocode

```plaintext
1. Initialize an array 'visitedBoxes' to keep track of opened boxes.
2. Start with the first box (index 0) and mark it as opened.
3. For each key in the first box, if the corresponding box is not in 'visitedBoxes', recursively open that box.
4. Repeat the process until all reachable boxes are opened or no more keys can be found.
5. If 'visitedBoxes' contains all box indices, return true; otherwise, return false.
```

## Code Implementation

```javascript
function canUnlockAll(boxes) {
  const visitedBoxes = [];

  function exploreBox(boxIndex) {
    if (visitedBoxes.includes(boxIndex)) {
      return;
    }

    visitedBoxes.push(boxIndex);

    for (const key of boxes[boxIndex]) {
      exploreBox(key);
    }
  }

  exploreBox(0);

  return visitedBoxes.length === boxes.length;
}
```

## Testing

```javascript
const boxes1 = [
  [1],
  [2],
  [],
  [0],
];

console.log(canUnlockAll(boxes1));  // Output: true

const boxes2 = [
  [1, 2],
  [3],
  [],
  [0],
];

console.log(canUnlockAll(boxes2));  // Output: false
```

## Conclusion

The `canUnlockAll` function solves the lockboxes problem efficiently using depth-first search. It explores the keys recursively and checks whether all boxes can be opened. This algorithm has a time complexity of O(N + K), where N is the number of boxes, and K is the total number of keys in all boxes.
