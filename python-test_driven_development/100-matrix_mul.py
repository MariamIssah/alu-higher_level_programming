#!/usr/bin/python3

"""Matrix multiplication without numpy module."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        list: Result of matrix multiplication.

    Raises:
        TypeError: If inputs are not lists of lists of numbers or if rows of matrices have inconsistent lengths.
        ValueError: If matrices are empty or cannot be multiplied.

    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    # Check if m_a and m_b are non-empty lists
    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")

    # Check if each element in m_a and m_b is a list of numbers
    for row in m_a + m_b:
        if not isinstance(row, list) or not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a and m_b should contain only integers or floats")

    # Check if each row of m_a has the same length
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must should be of the same size")

    # Check if each row of m_b has the same length
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must should be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(element)
        result.append(row)

    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: ./100-matrix_mul.py <m_a> <m_b>")
        sys.exit(1)

    m_a = eval(sys.argv[1])
    m_b = eval(sys.argv[2])

    print(matrix_mul(m_a, m_b))
