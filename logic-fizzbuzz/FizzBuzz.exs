(1..100) |> Enum.each(fn (ii) -> cond do
    rem(ii, 15) === 0 -> IO.puts "FizzBuzz"
    rem(ii, 3) === 0 -> IO.puts "Fizz"
    rem(ii, 5) === 0 -> IO.puts "Buzz"
    true -> IO.puts ii
  end
end)
