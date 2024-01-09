%14.Definiti un predicat care determina predecesorul unui numar reprezentat
%cifra cu cifra intr-o lista. De ex: [1 9 3 6 0 0] => [1 9 3 5 9 9].

adauga_sf(E,[],[E]):-!.
adauga_sf(E,[H|T],[H|L]):-adauga_sf(E,T,L).

invers([],[]):-!.
invers([H|T],L):-invers(T,L1), adauga_sf(H,L1,L).

pred([],[],_):-!.
pred([H|T],[H|L],N):-
	N=0,
	!,
	pred(T,L,0).
pred([H|T],[M|L],N):-
	N = 1,
	N =< H,
	!,
	M is H-N,
	pred(T,L,0).
pred([H|T],[M|L],N):-
	N=1,
	H=0,
	M is 10-N,
	pred(T,L,1).

predec([],[]):-!.
predec(L,R):-invers(L,L1),pred(L1,S,1),invers(S,R).
