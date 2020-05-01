// P733
var floodFill = function(image, sr, sc, newColor) {

    var flood = function(image, sr, sc, oldColor, newColor) {
        if (image[sr][sc] == oldColor) {
            image[sr][sc] = newColor;

            // up
            if (sr - 1 >= 0) { flood(image, sr-1, sc, oldColor, newColor) };

            // down
            if (sr + 1 < image.length) { flood(image, sr+1, sc, oldColor, newColor) };

            // left
            if (sc - 1 >= 0) { flood(image, sr, sc-1, oldColor, newColor) };

            // right
            if (sc + 1 < image[0].length) { flood(image, sr, sc+1, oldColor, newColor) };

        }

        return image
    }

    const oldColor = image[sr][sc]

    if ( oldColor == newColor) { return image}

    return flood(image, sr, sc, oldColor, newColor)

};








// app.js
var main = function(){

    // P733
    // var image = [[1,1,1],[1,0,1],[1,0,1]]
    // var sr = 1
    // var sc = 1
    // var newColor = 5

    var image = [[1,1,1],[1,1,0],[1,1,1]]
    var sr = 1
    var sc = 1
    var newColor = 5

    console.log(floodFill(image, sr, sc, newColor))


    
}

main()
