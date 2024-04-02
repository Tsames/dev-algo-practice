/*

Lodash provides a utility called dropWhile that creates a slice of an array with
elements dropped from the beginning until the predicate function returns falsey.

Your task is to implement a JavaScript function dropWhile that behaves like Lodash's
dropWhile utility using the following function signature:

dropWhile(array, predicate);
The function takes two arguments:

array: The array to iterate over.
predicate: The predicate is invoked with three arguments: (value, index, array) and returns a boolean value.
Your function should drop elements from the beginning of the array until the predicate function
returns falsey, and return the remaining elements as a new array. Your function should not modify the original array.

Examples
dropWhile([1, 2, 3, 4, 5], (value) => value < 3); // => [3, 4, 5]
dropWhile([1, 2, 3], (value) => value < 6); // => []
Note that Lodash's dropWhile utility also allows you to pass an optional thisArg parameter to bind this inside the predicate function, but for this exercise, you can ignore that parameter.

*/

export default function dropWhile<T>(array: Array<T>, predicate: (value?: T) => boolean): T[] {
  const output: Array<T> = [];
  let check = true;

  for (let i=0; i < array.length; i++) {
    check = check === true ? predicate.call(this, array[i], i, array) : false;
    if (!check) {
      output.push(array[i]);
    }
  }

  return output;
}