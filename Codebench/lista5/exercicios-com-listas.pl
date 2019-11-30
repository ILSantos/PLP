ultimo([X],X).           
ultimo([_|Y],X):-ultimo(Y,X).

iesimo([X|_],0,X).
iesimo([_|Y],N,X) :- iesimo(Y,M,X),
N is M + 1.

ordem([_]).
ordem([X,Y|Z]):- X =< Y , ordem([Y|Z]).
