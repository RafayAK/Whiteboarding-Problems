def binary_search(alist, item)
  alist = alist.sort

  first = 0
  last = alist.length - 1

  while first <= last
    midpoint = (first + last)/2
    if alist[midpoint] == item
      return true
    elsif alist[midpoint] < item
      first = midpoint + 1
    else
      last = midpoint -1
    end
  end

  false
end

testlist = [45, 6, -1, 0, 1, 2, 8, 0, 9, -3, 13, 17, 19, 32, 42,]
puts binary_search(testlist, 3)
puts binary_search(testlist, 13)