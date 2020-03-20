import statistics
from numpy import cov as covariance

def linreg(trainset, predictset):
    return

def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    x_mean = statistics.mean(x)
    y_mean = statistics.mean(y)
    b1 = covariance(x, y)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]

def test():
    return

# Runs test function
if __name__ == '__main__':
    test()
