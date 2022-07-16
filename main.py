def first_non_consecutive(arr):
    """
    Your task is to find the first element of an array that is not consecutive.

    By not consecutive we mean not exactly 1 larger than the previous element of the array.
    :param arr:
    :return:
    """
    first = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[first] == 1:
            pass
        else:
            return arr[i]
        first = i
    return None
