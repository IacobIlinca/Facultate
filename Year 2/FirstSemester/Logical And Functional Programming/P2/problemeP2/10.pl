%10.Se da o lista de numere intregi. Se cere sa se adauge in lista dupa 1-ul
% element, al 3-lea element, al 7-lea elemen, al 15-lea element … o
% valoare data e.

adaug_aux([],_,_,_,[]).
adaug_aux([H|T],V,P,C,[H|[V|LR]]):-
	C = P,
	!,
	C1 is C+1,
	P2 is P*2+1,
	adaug_aux(T,V,P2,C1,LR).
adaug_aux([H|T],V,P,C,[H|LR]):-
	C\=P,
	C1 is C+1,
	adaug_aux(T,V,P,C1,LR).

adaug(L,V,LR):-adaug_aux(L,V,1,1,LR).


