various_nums = [77.5, 92, 80, -78.111, 690, 101.3, -3.1515027, 0.0003, 23443]

for index in range (len(various_nums)):
    print(f"Item# {index} is {various_nums[index]}")
    print(f"item# {index} is {various_nums[index]:+}")
    print(f"item# {index} is {various_nums[index]: }")
    print(f"item# {index} is {various_nums[index]:<20.7f}")
    print(f"item# {index} is {various_nums[index]:>20.7f}")
    print(f"item# {index} is {various_nums[index]:20.7f}")
    print(f"item# {index} is {various_nums[index]:^20,.7f}")
    print("=" * 30)