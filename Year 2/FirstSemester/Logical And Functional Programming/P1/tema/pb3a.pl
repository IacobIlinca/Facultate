%apare(E:Intreg, L:Lista);
%Model de fux: (i,i);
%E:elementul pe care il verificam daca apare in lista
%L:lista in care verificam aparitia elementului;
apare(E,[E|_]):-!.
apare(E,[_|T]):-apare(E,T).


%multime(L:Lista, R:Lista);
%model de flux: (i,i), (i,o);
%L:lista intiala;
%R:lista creata ca multime, oridne inversata.
multime([],[]):-!.
multime([H],[H]):-!.
multime([H|T],R):-multime(T,R),apare(H,R),!.
multime([H|T],[H|R]):-multime(T,R),!.


%adauga_sfarsit(E:Intreg, L:Lista, LRez:Lista);
%Model de fux: (i,i,o);
%E:elementul ce se doreste a fi adaugat la finalul listei;
%L:lista initiala
%LRez: lista initlala cu elementul nou la final;
adauga_sf(E,[],[E]):-!.
adauga_sf(E,[H|T],[H|L]):-adauga_sf(E,T,L).


%invers(L:Lista. LRez:Lista);
%Model de flux: (i,o);
%L:lista intiala;
%LRez:lista inversata;
invers([],[]):-!.
invers([H|T],L):-invers(T,S),adauga_sf(H,S,L).

%multime(L:Lista, LRez: Lista);
%L:lista initiala
%LRez:lista transformata in multime in functie de I aparitie in ordine;
%in ordinea corecta.
multime_final([],[]):-!.
multime_final([H],[H]):-!.
multime_final(T,R):-invers(T,S),multime(S,L),invers(L,R).




