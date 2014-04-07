def substring(string, start=0, stop=None):
    '''
    Write a function named substring which takes (string, start, end)
    as arguments and returns the appropriate substring.

    >>> substring('hello world', 3, 7) 
    'lo w'

    If end is omitted, default to the end of the string:

    >>> substring('hello world', 3) 
    'lo world'

    If both start and end are omitted, return the whole string:

    >>> substring('hello world')
    'hello world'

    Negative indexes can be used to refer to positions relative to the
    end of the string:

    >>> substring('hello world', 1, -1)
    'ello worl'

    Negative indexes can be used in conjunction with a default end index:

    >>> substring('hello world', -4)
    'orld'

    Don't use string slicing (e.g. 'hello world'[1:-1]) in your
    implementation: that would be cheating!
    '''
    if stop is None:
        stop = len(string)

    if start < 0:
        start += len(string)
    if stop < 0:
        stop += len(string)
        
    return "".join([string[idx] for idx in range(start, stop)])



if __name__ == '__main__': 
    import doctest
    doctest.testmod()
