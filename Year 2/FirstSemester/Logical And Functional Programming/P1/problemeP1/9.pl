%9.a. Sa se scrie un predicat care intoarce intersectia a doua multimi.
% b. Sa se construiasca lista (m, ..., n), adica multimea numerelor
% intregi din intervalul [m, n].
%
%apartine(E:Integer, L:List).
apartine(E,[E|_]):-!.
apartine(E,[_|T]):-apartine(E,T).

%inters(L1:List, L2:List, LR:List).
inters([],_,[]).
inters([H|T],L2,[H|LR]):-apartine(H,L2),!, inters(T,L2,LR).
inters([H|T],L2,LR):-not(apartine(H,L2)),inters(T,L2,LR).

%b.
%interval(M:Integer,N:Integer, L:List).
interval(M,N,L):- M>N,!,L =[].
interval(M,N,L):- M=N,!, L=[M].
interval(M,N,[H|T]):- M<N,!, H=M, M2 is M+1, interval(M2,N,T).
