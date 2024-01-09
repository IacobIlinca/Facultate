;14.
;a.Dandu-se o lista liniare, se cere sa se elimine elementele din N in N.

(defun sterg (l n p)
    (cond
    ((null l)nil)
    (( = (mod p n) 0) (sterg (cdr l) n (+ p 1)))
    (t (cons (car l) (sterg (cdr l) n (+ p 1))))
    )
)

(defun sterge (l n)
    (sterg l n 1)
)        

;b.Sa  se  scrie  o  functie  care  sa  testeze  daca  o  lista  liniara  formata  din numere intregi are aspect de "vale"(o secvență se spune ca are aspect de "vale" daca elementele descresc pana la un moment dat, apoi cresc. De ex. 10 8 6 17 19 20).

(defun vale(l)
	(cond
		( ( null l ) nil )
		( ( > ( car l ) ( cadr l ) ) ( cobor2 l ) )
	)
)

(defun cobor2(l)
	(cond
		( ( null ( cdr l ) ) nil )
		( ( > ( car l ) ( cadr l ) ) ( cobor2 ( cdr l ) ) )
		( ( < ( car l ) ( cadr l ) ) ( urc2 l ) )
	)
)

(defun urc2(l)
	(cond
		( ( null ( cdr l ) ) t )
		( ( < ( car l) ( cadr l ) ) ( urc2 ( cdr l ) ) )
	)
)

;c.Sa  se  construiasca  o  functie  care  intoarce  minimul  atomilor  numerici dintr-o lista, de la orice nivel.

(defun minim (l)
    (cond
    ((null l) 320000)
    ((numberp (car l)) (min (car l) (minim (cdr l))))
    ((atom (car l)) (minim (cdr l)))
    (t (min (minim (car l)) (minim (cdr l))))
    )
)    

;d.Sa se scrie o functie care sterge dintr-o lista liniara toate aparitiile elementului maxim numeric.
(defun maxi (a b)
    (cond
    ((> a b) a)
    (t b)
    )
)
    
(defun maxim (l)
    (cond 
    ((null l) -320000)
    ((numberp (car l)) (maxi (car l) (maxim (cdr l))))
    ((atom (car l)) (maxim (cdr l)))
    (t (maxi (maxim (car l)) (maxim (cdr l))))
    )
) 

(defun sterg_max (l copie)
    (cond
    ((null l)nil)
    ((equal (car l) (maxim copie)) (sterg_max (cdr l) copie))
    (t (cons (car l) (sterg_max (cdr l) copie)))
    )
)    
    



