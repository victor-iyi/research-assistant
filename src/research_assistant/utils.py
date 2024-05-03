import math


def convert_size(size_bytes: int) -> str:
    """Converts the size of a file to a human-readable format.

    Args:
        size_bytes (int): The size of a file in bytes.

    Returns:
        str: The size of a file in a human-readable format.

    """

    if size_bytes == 0:
        return '0B'
    size_name = ('B', 'KB', 'MB')

    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)

    return f'{s} {size_name[i]}'
