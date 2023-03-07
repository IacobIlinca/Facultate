%15. a. Sa se scrie un predicat care se va satisface daca o lista are numar
% par de elemente si va esua in caz contrar, fara sa se numere elementele
% listei.
% b. Sa se elimine prima aparitie a elementului minim dintr-o lista de
% numere intregi.

%a.
par([]).
par([_|[_|T]]):-par(T).

%b.
min([],3200):-!.
min([H|T],H):-min(T,M), H<M,!.
min([_|T],M):-min(T,M).

elim([],_,[]):-!.
elim([H|T],M,T):-M=H,!.
elim([H|T],M,[H|L]):-H\=M, elim(T,M,L).

elimina([],[]):-!.
elimina(L,R):-min(L,M),elim(L,M,R).
