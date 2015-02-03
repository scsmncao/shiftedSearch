
def shiftedBinarySearch(shiftedList):

	# take the middle index
	mid = len(shiftedList)//2

	# this is the base case, if the len of the list is 1 or 2, just return the maximum of the two
	if len(shiftedList) == 2 or len(shiftedList) == 1:
		return max(shiftedList)

	# we divide the list into two
	# this checks to see if the first element of the first half is greater than the last element
	elif shiftedList[0] > shiftedList[mid]:

		# if it is, called shiftedBinarySearch on that half since we know the greatest integer is in that half
		return shiftedBinarySearch(shiftedList[0:mid+1])

	# this checks the upper half and also checks the first and last element
	elif shiftedList[mid + 1] > shiftedList[len(shiftedList) - 1]:
		return shiftedBinarySearch(shiftedList[mid+1:])

	# if they are both ordered, it either means we are right on the rotation or the list was the same before and after it was shifted
	# so just return the maximum of the mid number and last element
	else:
		return max(shiftedList[mid], shiftedList[len(shiftedList) - 1])
