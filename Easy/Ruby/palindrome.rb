# A palindrome is a word that is spelled the same backwards and forwards.

# Return true if word is palindrome, else return false.
def is_palindrome(word)
  word == word.reverse ? true : false
end

# ALTERNATIVE SOLUTION:
# This is way less ruby

# def is_palindrome(word)
#   i = 0
#   j = -1
#   while i < word.length/2
#     if word[i] == word[j]
#       i += 1
#       j -= 1
#     else
#       return false
#     end
#   end
# end

puts is_palindrome("a")
# true
puts is_palindrome("noon")
# true
puts is_palindrome("racecar")
# true
puts is_palindrome("porcupine")
# false
puts is_palindrome("Racecar")
# false