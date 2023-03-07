% Sa se genereze toate sirurile de n paranteze ce se inchid corect.
% Exemplu: n=4 sunt 2 solutii: (()) si ()().

%verif(N:Intreg,D:Intreg,I:Intreg,R:Lista).
%N:numarul de paranteze cu care vrem sa se genereze secventa.
%D:numarul de paranteze deschise.
%I:numarul de paranteze inchise.
%R:lista rezultat(o varianta de aranjare de paranteze).
%Model de flux: (i,o,o,o).
verif(N,N,N,[]):-!.
verif(N,D,I,['('|X]):-
	D<N,
	D1 is D+1,
	verif(N,D1,I,X).
verif(N,D,I,[')'|X]):-
	I<D,
	D =< N,
	I1 is I+1,
	verif(N,D,I1,X).


%paranteze(N:Intreg, R:Lista).
%N:numarul de paranteze dupa care sa se genereze secventa.
%R:lista rezultat(o varianta de aranjare de paranteze).
%Model de flux: (i,o).
paranteze(N,R):-N mod 2 =:= 0,
	N2 is N/2,
	verif(N2,0,0,R).

%toate(X:Intreg, Rez:Lista).
%X:numarul de paranteze dupa care sa se genereze secventa.
%Rez:lista rezultat(o varianta de aranjare de paranteze).
%Model de flux: (i,o).
toate(X,Rez):-findall(L,paranteze(X,L),Rez).
