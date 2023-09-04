def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    # ????
    res = b''
    for i in range(0, 4):
        for j in range(0, 4):
            res += bytes([matrix[i][j]])
    return res
