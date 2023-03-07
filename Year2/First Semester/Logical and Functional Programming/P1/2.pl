%2.a.Sa se scrie un predicat care determina cel mai mic multiplu comun al
%elementelor unei liste formate din numere intregi.
%b. Sa se scrie un predicat care adauga dupa 1-ul, al 2-lea, al 4-lea, al
%8-lea ...element al unei liste o valoare v data.

%cmmdc(E1:Integer, E2:Integer, R:Integer).
cmmdc(A,B,A):- A=B,!.
cmmdc(A,B,D):- A<B ,!, B1 is B-A , cmmdc(A,B1,D).
cmmdc(A,B,D):- A>B ,!,A1 is A-B, cmmdc(A1,B,D).

%cmmmc(E:Integer, F:Integer, R:Integer).
cmmmc(A,B,M):- P is A*B, cmmdc(A,B,D), M is P/D.

%cmmmcList(L:List, E:Integer).
cmmmcList([],1).
cmmmcList([H|T],R):-cmmmcList(T,S),cmmmc(H,S,R).

%b
%adaug_aux(L:List, V:Integer, P:Integer, C:Integer, LR:List).
adaug_aux([],_,_,_,[]).
adaug_aux([H|T],V,P,C,[H|[V|L]]):-
	P=C,
	!,
	P2 is P*2,
	C2 is C+1,
	adaug_aux(T,V,P2,C2,L).
adaug_aux([H|T],V,P,C,[H|L]):-
	not(P = C),
	!,
	C2 is C+1,
	adaug_aux(T,V,P,C2,L).

adaug(L,V,R):-
	P = 1,
	C = 1,
	adaug_aux(L,V,P,C,R).

