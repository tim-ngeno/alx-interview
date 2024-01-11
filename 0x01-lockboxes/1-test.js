import { canUnlockAll } from './1-lockboxes';

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
