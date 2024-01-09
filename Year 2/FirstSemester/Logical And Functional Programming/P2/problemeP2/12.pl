%12.Sa se inlocuiasca toate aparitiile unui element dintr-o lista cu un alt
%element.


%modif(L:List,E:Integer,V:Integer,R:List).
modif([],_,_,[]):-!.
modif([H|T],E,V,[M|L]):-
	H = E,!,
	M = V,
	modif(T,E,V,L).
modif([H|T],E,V,[H|L]):-
	H\=E,!,
	modif(T,E,V,L).
