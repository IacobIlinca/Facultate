%4.a. Sa se scrie un predicat care substituie intr-o lista un element printr-o
%alta lista.
%b. Sa se elimine elementul de pe pozitia a n-a a unei liste liniare.

%concatenare(L1:List,L2:List,LR:List).
concatenare([],L,L).
concatenare([H|T],L1,[H|R]):-concatenare(T,L1,R).

%subst(E:Integer, L1:List, L2:List,LR:List).
subst(_,_,[],[]).
subst(E,L,[E|T],R):-
	subst(E,L,T,R1),
	!,
	concatenare(L,R1,R).
subst(E,L,[H|T],[H|R]):- subst(E,L,T,R).

%b
%elimina(L:List, E:Integer, R:List).
elimina([],_,[]).
elimina([_|T],1,T):-!.
elimina([H|T],N,[H|L]):- N1 is N-1, elimina(T,N1,L).



