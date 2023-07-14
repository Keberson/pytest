def cat(str1: str, str2: str) -> str:
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("invalid type of args")

    return str1 + str2
