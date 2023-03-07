%4.a) Sa se interclaseze fara pastrarea dublurilor doua liste sortate.

intera([],[],[]).
intera(L,[],L).
intera([],L,L).
intera([H|T],[H1|T1],[H|L]):-H<H1,intera(T,[H1|T1],L),!.
intera([H|T],[H1|T1],[H1|L]):-H>H1,intera([H|T],T1,L),!.
intera([H|T],[H1|T1],[H|[H1|L]]):-H=H1,intera(T,T1,L),!.
