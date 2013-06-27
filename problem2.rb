#!/usr/bin/env ruby

limit = ARGV[0].to_i
puts "The limit is #{limit}"

exit unless limit


fib = Enumerator.new do |y|
	a = b = 1
	loop do
		y << a
		a, b = b, a + b
	end
end

sum = 0;

fib.each do |i|
	raise StopIteration if i > limit
	sum += i if i%2 == 0
end

puts "The result is #{sum}"
