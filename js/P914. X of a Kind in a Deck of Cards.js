// ToDo:
/* */

// Problem Description
/*
914. X of a Kind in a Deck of Cards
Easy

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

    Each group has exactly X cards.
    All the cards in each group have the same integer.

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.

Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.

Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].

Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].

Constraints:

    1 <= deck.length <= 10^4
    0 <= deck[i] < 10^4

*/

// Conditions & Concepts
/* 

*/

// Code
// submit part
/**
 * @param {number[]} deck
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    
};

// test part
/* */

// code here
// 1
/* 
Wrong Answer
Input: [0,0,0,0,0,1,1,2,3,4]
Output: true
Expected: false

Wrong Answer
Input: [1,1,1,1,2,2,2,2,2,2]
Output: false
Expected: true

Wrong Answer
Input: [0,0,0,0,1,1,2,2,3,3]
Output: false
Expected: true

Success
Runtime: 128 ms, faster than 13.45% of JavaScript online submissions for X of a Kind in a Deck of Cards.
Memory Usage: 43.7 MB, less than 5.85% of JavaScript online submissions for X of a Kind in a Deck of Cards.
*/
var hasGroupsSizeX = function(deck) {
  if ( deck.length <= 1 ) return false;

  const deckSet = new Set(deck);
  // if (  deckSet.size === deck.length || deck.length % deckSet.size !==0 ) return false;
  if (  (deck.length - deckSet.size) < deckSet.size ) return false;

  const findGcd = (...arr) => {
    const _gcd = (x, y) => (!y ? x : findGcd(y, x % y));
    return [...arr].reduce((a, b) => _gcd(a, b));
  };

  let groupNum; // X
  let res = true;
  deckSet.forEach( num => {
    if (!res) return;
    let count = 0
    while ( deck.indexOf(num) >= 0 ){
      let i = deck.indexOf(num);
      deck.splice(i, 1);
      count += 1;
    };
    if (groupNum === undefined) groupNum = count;

    // find gretest common factor
    if ( groupNum!==count ) {
      let gcd = findGcd(groupNum, count);

      // console.log({num, groupNum, count, gcd})

      if (gcd !== 1) groupNum = gcd;
      else res = false;
    }
  });
  
  return res;
};



// Test
var inputNums = [
  [1,2,3,4,4,3,2,1], 
  [1,1,1,2,2,2,3,3], 
  [1], 
  [1,1],  
  [1,1,2,2,2,2],
  [0,0,0,0,0,1,1,2,3,4],
  [1,1,1,1,2,2,2,2,2,2],
  [0,0,0,0,1,1,2,2,3,3],
];
var outputNums = [true, false, false, true, true, false, true, true]

var main = (fn = hasGroupsSizeX) => {
  for ( let i=0; i< inputNums.length; i++ ){
      if ( fn(inputNums[i]) === outputNums[i] ) console.log('Right.');
      else console.log('Wrong!');
  }
};

main();