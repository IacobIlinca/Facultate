%15.Sa se determine cea mai lunga secventa de numere pare consecutive
%% dintr-o lista (daca sunt mai multe secvente de lungime maxima, una
%% dintre ele).


lungime([],0):-!.
lungime([_|T],N):-lungime(T,N1),N is N1+1.

secv([],[],_):-!.
secv([H1|[H2|[H3|T]]],L,M):-
	H1 mod 2 =:= 0,
	H2 mod 2 =:= 0,
	H3 mod 2 =:= 0,
	!,
	M1 is M+1,
	L1 = [H1|L],
	secv(T,L1,M1).

secv([H1|[H2|[H3|T]]],L,M):-
	H1 mod 2 =:= 0,
	H2 mod 2 =:= 0,
	H3 mod 2 =\= 0,

