if not matrix: return False
left, right = 0, len(matrix) * (len(matrix[0]))
cols = len(matrix[0])
while left < right:
    mid = int((left + right) / 2)
    if matrix[mid / cols][mid % cols] == target:
        return True
    if matrix[mid / cols][mid % cols] > target:
        right = mid
    else:
        left = mid + 1
return False