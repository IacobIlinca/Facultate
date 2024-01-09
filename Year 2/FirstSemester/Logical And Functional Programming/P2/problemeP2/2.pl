%2a.Sa se sorteze o lista cu pastrarea dublurilor. De ex: [4 2 6 2 3 4]
% =>[2 2 3 4 4 6];

%insert(E:Intreg, L:Lista, LR:Lista);
%E:elementul ce se doreste sa fie inserat in lista;
%L:lista initiala in care se doreste a fi adaugat elementul;
%LR:lista rezultata din adaugarea elementului E
%in ordine crescatoare, in lista initiala L;
%Model de flux: (i,i,o);
insert(E,[],[E]).
insert(E,[H|T],[E|[H|T]] ):- E =<H, !.
insert(E, [H|T],[H|R]) :- E>H, insert(E,T,R).

%sortare(L:Lista, LR:Lista);
%L:lista initiala ce se doreste a fi sortata;
%LR:lista rezultata dupa sortarea listei initiale L;
%Model de flux: (i,o), (i,i);
sortare([],[]).
sortare([H|T],R):- sortare(T,L), insert(H,L,R),!.


%2b.Se da o lista eterogena, formata din numereintregi si liste de numere. Sa se sorteze fiecare sublista cu pastrareadublurilor. De ex:[1, 2, [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] =>[1, 2, [1, 4, 4], 3, 6, [1, 3, 7, 9, 10], 5, [1, 1, 1], 7].
%sorta(L:heterogeneous, LR:Lista heterogeneous);
%L:lista initiala;
%LR:lista cu listele sortate;
%model de flux: (i,o);
sorta([],[]).
sorta([H|T], [H|L]):-
	number(H),
	!,
	sorta(T,L).
sorta([H|T],[L|R]):-
	is_list(H),
	!,
	sortare(H,L),
	sorta(T,R).
sorta([_|T],R):-sorta(T,R).

