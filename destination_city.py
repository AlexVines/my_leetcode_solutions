def destCity(paths) -> str:
    """
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going
from city Ai to city Bi.
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore,
there will be exactly one destination city.

    >>> destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
    'Sao Paulo'
    >>> destCity([["B","C"],["D","B"],["C","A"]])
    'A'
    >>> destCity([["A","Z"]])
    'Z'

    """
    starts = []
    re = []
    for route in paths:
        starts.append(route[0])
        re.append(route[-1])
    for j in re:
        if j not in starts:
            return j


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)