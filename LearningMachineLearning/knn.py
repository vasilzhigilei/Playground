from collections import Counter
import math

def knn(data, query, k):
    """
    A K-nearest-neighbor implementation. Takes in data in the form of a list of lists,
    a query, as well as how many nearest neighbors to find (k).
    :param data: list holding data points, which consist of lists of x-dimension variables
    :param query: list withholding last variable of a data point (what knn is trying to guess)
    :param k: number of nearest neighbors to use
    :return: k-closest distances, knn guess for the query
    """
    # List of distance & index lists
    distances = []

    for index, current in enumerate(data):
        distances.append([math.sqrt(pow(current[0] - query[0], 2)), index])

    # Sort distances in ascending order
    distances = sorted(distances)

    # Nearest k-neighbors only
    distances = distances[:k]

    return distances, Counter([data[i][1] for distance, i in distances]).most_common(1)[0][0]

def test():
    """
    Tests knn with an arbitrary hard-coded data set.
    Prints results as a side-effect.
    :return: None
    """
    # Age data with 5 different options, 0, 1, 2, 3, or 4
    clf_data = [
        [22, 2], [67, 1], [32, 4],
        [23, 1], [24, 4], [44, 3],
        [21, 3], [30, 2], [33, 3],
        [18, 1], [19, 1], [21, 3],
        [19, 1], [40, 2], [50, 2],
        [25, 0], [29, 1], [53, 3],
        [27, 4], [47, 0], [25, 2],
        [29, 3], [19, 3], [22, 4],
        [31, 0], [48, 4], [36, 1],
        [45, 0], [59, 2], [32, 0],
    ]

    clf_query = [33]
    clf_k_nearest_neighbors, clf_prediction = knn(clf_data, clf_query, k=3)
    print("Nearest neighbors [distance, list-index] of query", clf_query[0], "are", clf_k_nearest_neighbors)
    print("Nearest neighbor data:")
    for distance, i in clf_k_nearest_neighbors:
        print(clf_data[i])
    print("Prediction of query:", clf_prediction)

# Runs test function
if __name__ == '__main__':
    test()