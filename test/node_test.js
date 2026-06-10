const assert = require('assert');
const { add } = require('../node/index');

assert.strictEqual(add(1, 2), 3, 'add(1,2) should be 3');
console.log('Node tests passed');
