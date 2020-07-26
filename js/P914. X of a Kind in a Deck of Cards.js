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
/* */
var hasGroupsSizeX = function(deck) {
    if ( deck.length === 1 ) { return false }
    
    let val = [];
    let count = []; 


    deck.forEach(function(ele){
        const i = val.indexOf
        if ( i === -1 ) {
            val.push(ele);
            count.push(1)
        } else {
            count[i] += 1
        }
    });

    const sameCount = count[0]

    for ( const c of count){
        if (c !== sameCount ){
            return false
        }
    }

    return true
};


// Test
var inputNums = [[1,2,3,4,4,3,2,1], [1,1,1,2,2,2,3,3], [1], [1,1],  [1,1,2,2,2,2]]
var outputNums = [true, false, false, true, true]

var main = function{
    for ( let i=0; i< inputNums.length; i++ ){
        if ( function(inputNums[i]) === outputNums[i] ){
            console.log('Right!')
        } else {
            console.log('Wrong!')
        }
    }
}