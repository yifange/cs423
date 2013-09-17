Toy.delete_all
(1..1000).each do |i|
  key = "KEY_#{i}"
  value = (0..300).map{('A'..'z').to_a[rand(58)]}.join
  puts key + "->" + value
  Toy.create(:key => "KEY_#{i}", :value => value)
end
