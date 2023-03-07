%13.a. Sa se scrie un predicat care transforma o lista intr-o multime, in
% ordinea ultimei aparitii. Exemplu: [1,2,3,1,2] e transformat in
% [3,1,2].
% b exact ca 10b.
%a.

aparitii(E,[E|_]).
aparitii(E,[_|T]):-aparitii(E,T).

multime([],[]).
multime([H|T],[H|L]):-not(aparitii(H,T)),!,multime(T,L).
multime([_|T],L):-multime(T,L).

