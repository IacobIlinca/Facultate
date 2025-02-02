%Sa se scrie un predicat care transforma o listaintr-o multime, in ordinea primei aparitii. Exemplu: [1,2,3,1,2] e transformat in [1,2,3].

%sterge(E:Intreg, L:Lista, LR:Lista);
%E:elementul care se doreste sa fie sters
%L:lista intiala, din care se va sterge elementul;
%LR:lista rezultata dupa stergerea elementului din lista initiala;
%Model de flux: (i,i,o);

sterge(_,[],[]):-!.
sterge(E,[E],[]):-!.
sterge(E,[H|T],[H|R]):- H=\=E, sterge(E,T,R).
sterge(E,[H|T],R):-H=:=E, sterge(E,T,R).


%multime(L:Lista, LR:Lista);
%L:lista initiala ce se doreste a fi modificata in multime;
%LR:lista rezultat, sub forma de multime,
%in functie de prima aparitie a elementelor;
%Model de flux: (i,o), (i,i);
multime([],[]):-!.
multime([H|T],[H|R]):-sterge(H,T,L), multime(L,R).
