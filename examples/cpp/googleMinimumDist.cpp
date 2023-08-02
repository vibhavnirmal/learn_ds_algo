// We have a line of blocks and each has specific places eg gym, school, office, etc.

// We have to find a block such that the sum of the distances from the block to all the places is minimum.

// lane = [{
//     gym: false,
//     school: true,
//     store: false
// },
// {
//     gym: true,
//     school: false,
//     store: false
// },
// {
//     gym: true,
//     school: true,
//     store: false
// },
// {
//     gym: false,
//     school: true,
//     store: false
// },
// {
//     gym: false,
//     school: true,
//     store: true
// }]

// places = ["gym", "school", "store"]

// Output: 3

// Explanation: The best place is block 3 because the school is 0 units away, gym is 1 unit away and store is 1 unit away. The least farthest distance to all places is max(0, 1, 1) = 1.

// Approach: We can use the brute force approach to solve this problem. We can find the distance of each block from all the places and then find the minimum of all the distances. The time complexity of this approach will be O(N*M) where N is the number of blocks and M is the number of places.