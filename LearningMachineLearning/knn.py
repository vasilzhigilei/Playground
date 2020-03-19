import statistics
import math

def knn(data, query, k):
    # List of distance & index lists
    distances = []

    for label, value in data:
        distances.append([math.sqrt(pow(label - query[0], 2) + pow(value, 2)), label])
    print(distances)
    # Sort distances in ascending order
    distances = sorted(distances)
    print(distances)
    return statistics.mode(distances[:k][1])

def test():
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
    print("Nearest neighbors of query " + clf_query[0] + " are " + clf_k_nearest_neighbors)
    print("Prediction of query: " + clf_prediction)

if __name__ == '__main__':
    test()