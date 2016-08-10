# Solution 1: Runtime O(n) Space complexity O(1)


def sum_in_range(n):

	sum_of_ints = 0
	for i in range(n):
		sum_of_ints += i

return sum_of_ints


# Sulution 2(Recursive): Runtime O(n) Space complexity O(n)  


def sum_in_range(n):

	if n <= o:
		return 0
	else:
		return n + sum_in_range(n - 1)


# Solution 3(Formula): Runtime O(1) Space complexity O(1)


def sum_in_range(n):

	sum_of_ints = ((n + 1) * n) / 2

# Solution 4(Generator Expression)

def sum_in_range(n):
	
	return sum(x for x in range(n))
