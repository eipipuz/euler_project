#!/usr/bin/env ruby

n = ARGV[0].to_i
exit unless n

def factorize(n, factors = [])
	max_factor = Math.sqrt(n).floor
	(2..max_factor).each do |i|
		if n % i == 0
			factors.push(i)
			n /= i
			return factorize(n, factors)
		end
	end

	factors.push(n)
end

factors = factorize(n)

puts "The largest prime factor of the number #{n} is #{factors[-1]}"
