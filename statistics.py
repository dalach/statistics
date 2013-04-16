"""These are some statistics functions for Coursera class."""

import math

def median(L):
    """(list of num)->float
    Returns a median value of the data list.

    >>> median([1,2,3,3,3,4,6])
    3.0
    >>> median([2,3])
    2.5
    """
    index = len(L)//2
    if len(L)%2 == 0:
        return (L[index] + L[index-1])/2.0
    else:
        return float(L[index])


def mean(L):
    """(list of num)->float
    Returns mean (average) of list's items.

    >>> mean([1,2,3])
    2.0
    >>> mean([-1, -3, -5])
    -3.0
    """
    list_sum = 0
    num_of_items = float(len(L))
    if num_of_items == 0:
        return 0
    else:
        for num in L:
            list_sum += num
        return list_sum/num_of_items

def trimmed_mean(L, n):
    """(list, int)->float
    Return mean for a data list without first n-elements and without last n-elements.
    Please notice, that we cut off an accurate number of elements, not the percentage.

    >>> trimmed_mean([1,2,3,4,5,6,7], 2)
    4.0
    """
    return mean(L[n:-n])

def first_quartile(L):
    """(list of num)->float
    Returns first quartile of the data list.

    >>> first_quartile([1,2,3,4,5])
    2
    """
    if len(L) % 2 == 0:
        index = 0.25 * (len(L) - 1)
        return L[int(math.floor(index))] + 0.25 * (L[int(math.ceil(index))] - L[int(math.floor(index))])
    else:
        return L[int(len(L)*0.25)]

def third_quartile(L):
    """(list of num)->float
    Returns third quartile of the data list.

    >>> third_quartile([1,2,3,4,5])
    4
    """
    if len(L) % 2 == 0:
        index = 0.75 * (len(L) - 1)
        return L[int(math.floor(index))] + 0.75 * (L[int(math.ceil(index))] - L[int(math.floor(index))])
    else:
        return L[int(len(L)*0.75)]

# spread of data

def get_range(L):
    """(list of num)->float
    Returns range of values in the data list.
    
    >>> get_range([2,3,6,11])
    9.0
    >>> get_range([-2,-4,5,8])
    12.0
    """
    return float(max(L) - min(L))

def get_iqr(first_quartile, third_quartile):
    """(float, float)->float
    Return inner quartile range.

    >>> get_iqr(4, 5.5)
    1.5
    >>> get_iqr(-32, 59)
    91
    """
    return third_quartile - first_quartile

def variance(L):
    """(list of num)->float
    Returns variance for the data list.
    """
    base = 0
    list_mean = mean(L)
    for number in L:
        base += (number - list_mean)**2
    return base/float(len(L)-1)

def standard_deviation(L):
    """(list of num)-> float
    Returns a standard deviation for the data list.

    """
    return math.sqrt(variance(L))


# learning from histograms

def is_left_skewed(mean, median):
    """(list of num)->bool
    Returns True if and only if histogram is left skewed.

    >>> is_left_skewed(7,3)
    False
    >>> is_left_skewed(3,7)
    True
    """ 
    return mean < median

def is_right_skewed(mean, median):
    """(list of num)->bool
    Returns True if and only if histogram is right skewed.

    >>> is_right_skewed(7,3)
    True
    >>> is_right_skewed(3,7)
    False
    """
    return mean > median

#uncomment lines below to test functions
"""
if __name__ == '__main__':
    import doctest
    doctest.testmod()

"""
