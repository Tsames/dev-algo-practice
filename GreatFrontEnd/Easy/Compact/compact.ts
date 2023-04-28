/*

Lodash's Compact method
In JavaScript, the Lodash library provides a utility function called compact, which removes
falsey values (i.e., values that evaluate to false in a boolean context) from an array.
Falsey values include false, null, 0, "", undefined, and NaN (you should know this by heart!).

Let's write our own version as a compact function. The function has the following signature:

compact(array);
Examples:

compact([0, 1, false, 2, '', 3, null]); // => [1, 2, 3]
compact(['hello', 123, [], {}, function () {}]); // => ['hello', 123, [], {}, function() {}]

*/

export default function compact(arry) {
  return arry.filter( (element) => {
    if (element) {
      return element
    }
  })
}