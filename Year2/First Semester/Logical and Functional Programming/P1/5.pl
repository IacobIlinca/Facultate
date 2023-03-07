%5a. Sa se scrie un predicat care sterge toate aparitiile unui anumit
% atom dintr-o lista. b. Definiti un predicat care, dintr-o lista de
% atomi, produce o lista de perechi (atom n), unde atom apare in lista
% initiala de n ori. De ex: numar([A B A B A C A], X) va produce X = [[A
% 4] [B 2] [C 1]].

%a.
%sterge(E:Integer, L:List, LR:List).

sterge(_, [],[]):-!.
sterge(E,[H|T],[H|T1]):-
	H \= E,
	!,
	sterge(E,T,T1).
sterge(E, [_|T],T1):-
	sterge(E,T,T1).

%b.
%nr_apar(E:integer, L:List, N:Integer).

nr_apar(_, [], 0).
nr_apar(E, [H|T],N):- H=E,nr_apar(E,T,NT),N is NT + 1,!.
nr_apar(E, [H|T], N):- H\= E,nr_apar(E,T,N).

%perechi(L:List, P:List).

perechi([], []):-!.
perechi([E],[[E,1]]):-!.
perechi([H|T],[[H,N1]|P]):-
	nr_apar(H,T,N),
	N1 is N+1,
	sterge(H,[H|T],L),
	!,
	perechi(L,P).


