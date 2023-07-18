"""
973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:

    1 <= k <= points.length <= 104
    -104 < xi, yi < 104
"""
from typing import List


class Solution:
    # Time complexity: O(N⋅logN) for the sorting of points.
    # Space complexity: O(logN) to O(N) for the extra space required by the sorting process.
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the list with a custom comparator function
        points.sort(key=self.squared_distance)

        # Return the first k elements of the sorted list
        return points[:k]

    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2


class Solution2:
    """
    Algorithm

    Precompute the Euclidean distances of each point.
    Define the initial binary search range by identifying the farthest computed distance.
    Perform a binary search from low to high using the reference distances.
        Calculate the midpoint of the remaining range as the target distance.
        Split the remaining points into those closer and those farther than the target distance.
        If the closer array has fewer than kkk points, add them to the closest array and adjust the value of kkk.
        Keep only the appropriate remaining array for the next iteration and update the binary search range.
    Once kkk elements have been added to the closest array, return the kkk closest points.

    Complexity Analysis

    Here N refers to the length of the given array points.

        Time complexity: O(N)
        This yields an average time complexity of O(N).

        Space complexity: O(N)
        An extra O(N) space is required for the arrays containing distances and reference indices.

    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Precompute the Euclidean distance for each point
        distances = [self.euclidean_distance(point) for point in points]
        # Create a reference list of point indices
        remaining = [i for i in range(len(points))]
        # Define the initial binary search range
        low, high = 0, max(distances)

        # Perform a binary search of the distances
        # to find the k closest points
        closest = []
        while k:
            mid = (low + high) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                # If more than k points are in the closer distances
                # then discard the farther points and continue
                remaining = closer
                high = mid
            else:
                # Add the closer points to the answer array and keep
                # searching the farther distances for the remaining points
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                low = mid

        # Return the k closest points using the reference indices
        return [points[i] for i in closest]

    def split_distances(self, remaining: List[int], distances: List[float],
                        mid: int) -> List[List[int]]:
        """Split the distances around the midpoint
        and return them in separate lists."""
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
        return [closer, farther]

    def euclidean_distance(self, point: List[int]) -> float:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2

