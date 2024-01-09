;16.Sa se decida daca un arbore de tipul (2) este echilibrat (diferenta dintre adancimile celor 2 subarbori nu este mai mare decat 1).

(defun adancime (l)
    (cond
    ((null l) 0)
    ((null (cdr l))1) ;e doar radacina
    (t (+ 1 (max (adancime (cadr l)) (adancime (caddr l)))))
    )
)    
    
(defun echi (l)
    (cond
    (( > 2 (abs ( - (adancime (cadr l)) (adancime (caddr l))))) 'echilibrat)
    (t 'ne-echilibrat)
    )
)    


(defun echilibrat(l)
	(cond
		( ( <= ( abs ( - (adancime ( cadr l ) ) ( adancime ( caddr l ) ) ) ) 1 ) 1 )
		( t nil )
	)
)