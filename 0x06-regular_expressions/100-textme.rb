#!/usr/bin/env ruby
# ?:(non-capture grouping)
# '(.*?)` - match everything in a non-greedy way and capture it

puts ARGV[0].scan(/\[(?:from|to|flags):(.*?)\]/ix).join(',')
