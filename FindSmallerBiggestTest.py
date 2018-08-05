from FindSmaller import find_smaller
from FindBiggest import find_biggest

numbers = [34, 54, 23, 2, 87, 34, 55, 235, 6643, 39]
smaller_index = find_smaller(numbers)
smaller = numbers[smaller_index]
print "Najmniejszy elemnt: ", smaller
biggest_index = find_biggest(numbers)
biggest = numbers[biggest_index]
print "Najwiekszy element: ", biggest