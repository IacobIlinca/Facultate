%1.aSa se scrie un predicat care intoarce diferenta a doua multimi.
%b.Sa se scrie un predicat care adauga intr-o lista dupa fiecare element par
%valoarea 1.

%a.
%member(E:Integer,L:List).
member(E,[E|_]):-!.
member(E,[_|T]):-member(E,T).

%diferenta(L1:List,L2:List, LR:List).
diferenta(L,[],L):-!.
diferenta([],_,[]).
diferenta([H|T],L,[H|T1]):-
	not(member(H,L)),
	!,
	diferenta(T,L,T1).
diferenta([_|T],L,L1):-diferenta(T,L,L1).

%b.
%adauga(L:List, LR:List).
adauga([],[]).
adauga([H|T],[H|[1|T1]]):-
	H mod 2 =:= 0,
	!,
	adauga(T,T1).
adauga([H|T],[H|T1]):-adauga(T,T1).


