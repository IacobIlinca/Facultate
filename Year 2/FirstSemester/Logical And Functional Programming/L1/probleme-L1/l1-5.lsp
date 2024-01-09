;5.
;a.Definiti o functie care interclaseaza cu pastrarea dublurilor doua liste liniare sortate.

(defun inter(l1 l2)
	(cond
		( ( null l1 ) l2 )
		( ( null l2 ) l1 )
		( ( <= ( car l1 ) ( car l2 ) ) ( cons ( car l1 ) ( inter ( cdr l1 ) l2 ) ) )
		( ( <= ( car l2 ) ( car l1 ) ) ( cons ( car l2 ) ( inter l1 ( cdr l2 ) ) ) )
		( t ( cons ( car l1 ) ( car l2 ) ( inter ( cdr l1 ) (cdr l2 ) ) ) )
	)
)	

;b.Definiti o functie care substituie un element E prin elementele unei liste L1 la toate nivelurile unei liste date L.

(defun inloc (l e l1)
    (cond
    ((null l)nil)
    ((equal (car l) e) (append l1 (inloc (cdr l) e l1)))
    ((atom (car l)) (cons (car l) (inloc (cdr l) e l1)))
    (t( cons (inloc (car l) e l1) (inloc (cdr l) e l1)))
        ;aici mergea si cu append
    )
)    

;c.Definiti o functie care determina suma a doua numere in reprezentare de lista si calculeaza numarul zecimal corespunzator sumei.

;d. Definiti o functie care intoarce cel mai mare divizor comun al numerelor dintr-o lista liniara.


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