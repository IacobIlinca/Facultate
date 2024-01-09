;6.b. Sa  se  scrie  o  functie  care  realizeaza  o  lista  de  asociere  cu  cele  doua liste  pe  care  le  primeste.  De  ex:  (A  B  C)  (X  Y  Z) -->  ((A.X)  (B.Y) (C.Z)).
( defun p(l1 l2)
	( cond
		((null l1) nil )
		((null l2) nil )
		
		(t ( cons ( cons (car l1 ) (car l2 ) ) ( p ( cdr l1 ) (cdr l2 ) ) ) )
	)
)

;(p '(A B C) '(X Y Z))