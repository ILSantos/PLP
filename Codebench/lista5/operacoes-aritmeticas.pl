fatorial(0,1).
fatorial(N,F) :- N>0, 
   N1 is N-1,
   fatorial(N1,F1),
   F is N * F1.

mdc(X,0,Z) :- !, Z = X.
mdc(X,Y,Z) :- R is X mod Y, mdc(Y,R,Z).


fib(0, 0) :- !.
fib(1, 1) :- !.
fib(N, Result) :- N1 is N - 1, N2 is N - 2, fib(N1, Result1), fib(N2, Result2), Result is Result1 + Result2.
