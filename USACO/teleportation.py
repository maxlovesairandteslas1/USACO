file_in = open('teleport.in')
data = file_in.read().strip().split('\n')
a, b, x, y = map(int, data[0].split(' '))

# Manually sort a, b to be increasing order
if a > b:
	a, b = b, a

# Manually sort x, y to be increasing order
if x > y:
	x, y = y, x

# Set base distance as distance needed to travel without using teleporter
base_distance = abs(a - b)

# Set teleporter distance to be the travel distance using the teleporter
teleporter_distance = abs(a - x) + abs(b - y)

# The answer is the minimum of the teleporter distance and the base distance
ans = min(teleporter_distance, base_distance)

# Output the answer using Python file i/o system
print(ans, file = open('teleport.out', 'w'))