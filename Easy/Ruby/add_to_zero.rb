# Given array of ints, return True if any two nums in list sum to 0.

def sum_zero(array)
  array.empty? ? false : compare(array)
end

def compare(array)
  our_set = {}

  array.each do |integer|
    if our_set.key?(-integer)
      return true
    end
    our_set[integer] = 0
  end
  false
end

sum_zero([])
sum_zero([1,2])
sum_zero([-1,0,1])