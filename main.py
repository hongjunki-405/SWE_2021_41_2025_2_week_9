from typing import List

def even_list(int_list: List[int]) -> List[int]:
    """Return only even integers from int_list."""
    # TODO: implement in a feature branch
    pass

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """Return sum of squares of all even numbers."""
    # TODO: implement in a feature branch
    pass

def main():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    even_ints = even_list(int_list)
    output = sum_of_squares_of_even(even_ints)
    print(output)

if __name__ == "__main__":
    main()
