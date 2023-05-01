/*
The Lodash _.difference() function is used to remove a single element or the array of elements
from the original array. This function works pretty much same as the core function of JavaScript i.e filter.

Let's write our own version as a difference function following the signature:

difference(array, [values]);
array: Array from which different elements are to be removed.
values: Array of values that are to be removed from the original array.

#### Examples: ####

difference(['a', 2, 3], [2, 3]); // => ["a"]
difference([1, , 3], [1]); // => [3]

The function should return the original array if the value array is empty array.

difference(['a', 2, 3], []); // => ["a", 2, 3]
*/

export default function difference(array: Array<any>, values: Array<any>): Array<any> {
  let output = [];

  for (let i=0; i < array.length; i++) {

    let present = false;
    for (let j=0; j < values.length && present == false; j++) {

      if (array[i] === values[j]) {
        present = true
      }

    }

    if (!present) output.push(array[i])
  }

  return output;
};