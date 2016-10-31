-module('FizzBuzz').
-export([main/0]).

main() ->
    args = lists:seq(1, 100).
    %% lists:foreach(fun(ii) -> io.format(ii) end, args)


    io:format("Heloo\n").
    %% lists:map(
    %%   fun(ii) -> io:format(ii) end,
    %%   lists:seq(1, 100)).
