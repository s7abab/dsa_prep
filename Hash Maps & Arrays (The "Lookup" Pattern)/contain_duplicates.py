nums = [1, 2, 3, 3]

def contain_duplicates(nums):
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)

    return False

print(contain_duplicates(nums))