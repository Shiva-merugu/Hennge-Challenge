import sys

def process_numbers(nums, index):
    if index == len(nums):
        return 0
    
    current = nums[index]
    
    if current < 0:
        return current**4 + process_numbers(nums, index + 1)
    else:
        return process_numbers(nums, index + 1)


def handle_test_cases(n):
    if n == 0:
        return
    
    x = int(input())   # number of elements
    nums = list(map(int, input().split()))
    
    result = process_numbers(nums, 0)
    print(result)
    
    handle_test_cases(n - 1)


def main():
    t = int(input())   # number of test cases
    handle_test_cases(t)


if __name__ == "__main__":
    main()
    