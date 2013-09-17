Toy.delete_all
puts "hahah"
(1..100).each do |key|
  puts "key"
  Toy.create(:key => "KEY_#{key}", :value => (0..300).map{('A'..'z').to_a[rand(58)]}.join)
end
