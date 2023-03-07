%7.Definiti un predicat care determina produsul unui numar reprezentat
% cifra cu cifra intr-o lista cu o anumita cifra. De ex: [1 9 3 5 9 9] * 2 => [3 8 7 1 9 8]

adauga_sf(E,[],[E]):-!.
adauga_sf(E,[H|T],[H|L]):-adauga_sf(E,T,L).

invers([],[]):-!.
invers([H|T],L):-invers(T,S),adauga_sf(H,S,L).

prod([],_,[],0):-!.
prod([],_,[N],N).
prod([H|T],V,[M|L],N):-
	N=0,
	!,
	P is V*H,
	M is P mod 10,
	N1 is P div 10,
	prod(T,V,L,N1).
prod([H|T],V,[M|L],N):-
	N\=0,
	!,
	P is V*H+N,
	M is P mod 10,
	N1 is P div 10,
	prod(T,V,L,N1).

produs([],_,[]):-!.
produs(L,V,R):-
	invers(L,S),
	prod(S,V,T,0),
	invers(T,R).
