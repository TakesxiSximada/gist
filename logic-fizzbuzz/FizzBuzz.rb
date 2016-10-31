#! /usr/bin/env ruby
(0..100).each do |ii|
  msg = ""
  if ii % 3 == 0
    msg += "Fizz"
  end
  if ii % 5 == 0
    msg += "Buzz"
  end
  puts msg.empty? ? ii : msg
end
