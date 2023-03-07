%8.Definiti un predicat care determina succesorul unui numar reprezentat
%cifra cu cifra intr-o lista. De ex: [1 9 3 5 9 9] => [1 9 3 6 0 0]


adauga_sf(E,[],[E]):-!.
adauga_sf(E,[H|T],[H|L]):-adauga_sf(E,T,L).

invers([],[]).
invers([H|T],L):-invers(T,L1),adauga_sf(H,L1,L).

succesor([],[]):-!.
succesor(L,R):-invers(L,S),suc(S,M,1),invers(M,R).

suc([],[],_):-!.
suc([H|T],[H|L],N):-N=0,!,suc(T,L,0).
suc([H|T],[M|L],N):-
	N\=0,
	!,
	S is N+H,
	M is S mod 10,
	N1 is S div 10,
	suc(T,L,N1).
