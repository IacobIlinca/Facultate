;6.
;a.Sa  se  scrie  de  doua  ori  elementul  de  pe  pozitia  a  n-a  a  unei  liste liniare. De exemplu, pentru (10 20 30 40 50) si n=3 se va produce (10 20 30 30 40 50).
(defun inter ( n l)
  (cond
	((null l) (nil))
	(( = n 1) (cons (car l) l))
	( t (append  (cons (car l) (inter (- n 1) (cdr l)))))
	)
)

;b.Sa  se  scrie  o  functie  care  realizeaza  o  lista  de  asociere  cu  cele  doua liste  pe  care  le  primeste.  De  ex:  (A  B  C)  (X  Y  Z) -->  ((A.X)  (B.Y) (C.Z)).

( defun p(l1 l2)
	( cond
		((null l1) nil )
		((null l2) nil )
		(t ( cons ( cons (car l1 ) (car l2 ) ) ( p ( cdr l1 ) (cdr l2 ) ) ) )
	)
)

;c.Sa  se  determine  numarul  tuturor  sublistelor  unei  liste  date,  pe  orice nivel. Prin sublista se intelege fie lista insasi, fie un element de pe orice nivel, care este lista. Exemplu: (12 (3 (4 5) (6 7)) 8 (9 10)) => 5 (lista insasi, (3 ...), (4 5), (6 7), (9 10)).

(defun nr_subliste(l)
  (cond 
    ((null l) 0)
    ((atom (car l)) (nr_subliste (cdr l)))  
   (t (+ (+ 1 (nr_subliste(car l))) (nr_subliste(cdr l))))
  )
)
(defun subliste(l)
  (+ 1 (nr_subliste l)) 
  ;adun 1--lista(insasi) mare e lista
)

;d.Sa se construiasca o functie care intoarce numarul atomilor dintr-o lista, de la nivel superficial.
(defun nratom(l)
  (cond
     ((null l) 0)
     ((atom (car l)) (+ 1 (nratom (cdr l))))
     (t (nratom (cdr l)))
  )
)