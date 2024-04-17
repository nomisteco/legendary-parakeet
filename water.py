def water_trap(list):
    total_height = 0

    #for each cell check the highest wall to the right and left
    for i in range(1, len(list)-1):
        max_left = max(list[:i]) # max from left to right
        max_right = max(list[i:])

        upper_bound = min(max_left, max_right)

        total_height += max(0, upper_bound - list[i])

    return total_height

print(water_trap([2, 0, 0, 4, 5]))
print(water_trap([2, 1, 2, 3, 4]))
print(water_trap([2, 5, 0, 4, 5]))


