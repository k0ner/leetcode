from typing import List


def is_in_sequence(array: List[int]) -> bool:
    def is_in_seq_rec(index: int) -> bool:
        if index >= len(array):
            return True
        return array[index - 1] == array[index] - 1 and is_in_seq_rec(index + 1)

    return is_in_seq_rec(1)


def sum_of_digits(number: int) -> int:
    if number < 0:
        return sum_of_digits(-number)
    if not number:
        return 0
    return number % 10 + sum_of_digits(number // 10)


if __name__ == '__main__':
    print(is_in_sequence(array=[2, 3, 4, 5, 6, 7]))
    print(is_in_sequence(array=[2, 4, 5, 6, 7]))
    print(sum_of_digits(123456))
    print(sum_of_digits(-123456))
