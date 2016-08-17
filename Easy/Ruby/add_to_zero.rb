# Given array of ints, return True if any two nums in list sum to 0.

require 'set'

def sum_zero(array)
  array.empty? ? false : compare(array)
end

def compare(array)
  our_set = Set.new

  array.each do |integer|
    if our_set.include?(-integer)
      return true
    end
    our_set.add(integer)
  end
  false
end

puts sum_zero([])
puts sum_zero([1, 2])
puts sum_zero([-1, 0, 1])
