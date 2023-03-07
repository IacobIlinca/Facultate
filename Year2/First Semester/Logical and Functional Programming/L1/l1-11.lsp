;11.
;a.Sa se determine cel mai mic multiplu comun al valorilor numerice dintr-o lista neliniara.

(defun cmmdc(a b)
	(cond
		( ( = a 0 ) b )
		( ( = b 0 ) a )
		( t ( cmmdc b (mod a b ) ) )
	)
)

(defun lcmmdc(l)
	( cond
		( ( null l ) 0 )
		( ( numberp l ) l )
		( t ( cmmdc ( car l ) ( lcmmdc ( cdr l ) ) ) )
	)
)

(defun cmmmc (a b)
    ( / ( * a b ) ( cmmdc a b ) )
)

(defun lcmmmc(l)
	(cond
		( ( null l ) 1 )
		( ( numberp l ) l )
		( t ( cmmmc ( car l ) ( lcmmmc ( cdr l ) ) ) )
	)
)

;b.Sa  se  scrie  o  functie  care  sa  testeze  daca  o  lista  liniara  formata  din numere intregi are aspect de "munte"(o secvență se spune ca are aspect de "munte" daca elementele cresc pana la un moment dat, apoi descresc. De ex.10 18 29 17 11 10).


( defun munte(l)
	( cond
		( ( null l ) nil )
		( ( < ( car l ) ( cadr l ) ) ( urc l ) )
	)
)

(defun urc(l)
	(cond
		( ( null ( cdr l ) ) f )
		( ( < ( car l ) ( cadr l ) ) ( urc ( cdr l ) ) )
		( ( < ( cadr l ) ( car l ) ) ( cobor l ) )
	)
)

(defun cobor(l)
	(cond
		( ( null ( cdr l ) ) t )
		( ( < ( cadr l ) ( car l ) ) ( cobor ( cdr l ) ) )
	)
)

;c.Sa  se  elimine  toate  aparitiile  elementului  numeric  maxim    dintr-o  lista neliniara.

(defun maxim(l)
    (cond
    ((null l) -99999)
    ((numberp (car l)) (max (car l) (maxim (cdr l))))
    (t (max (maxim (car l)) (maxim (cdr l))))
    )
)

(defun elimina (l copie)
    (cond
    ((null l)nil)
    ((and (numberp (car l)) (equal (car l) (maxim copie))) (elimina (cdr l) copie))
    ((atom (car l)) (cons (car l) (elimina (cdr l) copie)))
    (t(cons(elimina (car l) copie) (elimina (cdr l) copie)))
    )
)

(defun elim (l)
    (elimina l l)
)

;d.Sa se construiasca o functie care intoarce produsul atomilor numerici pari dintr-o lista, de la orice nivel.

(defun produs (l)
    (cond
    ((null l)1)
    ((and(numberp (car l))(=(mod (car l) 2)0)) (* (car l) (produs (cdr l))))
    ((atom (car l)) (produs (cdr l)))
    (t(*(produs (car l)) (produs (cdr l))))
    )
)    














    
