
def odd_nums(nums):
    n = 1
    while n <= nums:
        yield n
        n += 2


odd_to_15 = odd_nums(15)

