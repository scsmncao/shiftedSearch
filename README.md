 # Shifted Search

This algorithm uses a motified binary search to search for the largest element in a shifted list

 1. Edge cases would be:
 if all the elements were the same
 if the numbers were the same before and after the shift
 if the greatest number was at the ends of our list 
 we should make sure it works for even and odd length lists
 check for if there are duplicate maximums or duplicate numbers

 2. Using the master theorem:
 T/2 + O(1)
 this means that a = 1, b = 2, c = 0
 log base 2 of 1 is 0 which is equal to c
 so that means the complexity is O(n^clogn)
 so the orders of growth is O(logn)

 3. Another way to do it is to transverse through the list and find the pivot point but that's worst case O(n) which is worse than O(logn)
 You can sort the list first, but python's sort (Timsort) has a best case O(n) so that would require O(n) time
 I don't think this can be done in constant time so I think logn is the fastest you can do it.