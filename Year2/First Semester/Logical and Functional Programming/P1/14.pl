%14.a. Sa se scrie un predicat care testeaza egalitatea a doua multimi, fara
%sa se faca apel la diferenta a doua multimi.
%b. Definiti un predicat care selecteaza al n-lea element al unei liste.

egal([],[]).
egal([H|T],[H|T1]):-egal(T,T1).

member(E,[E|_]):-!.
member(E,[_|T]):-member(E,T).

mult([],_):-!.
mult([H|T],L):-member(H,L),mult(T,L).

egali(L1,L2):- mult(L1,L2),mult(L2,L1).

alN([H|_],1,P):-P=H,!.
alN([_|T],N,P):-N1 is N-1, alN(T,N1,P).
