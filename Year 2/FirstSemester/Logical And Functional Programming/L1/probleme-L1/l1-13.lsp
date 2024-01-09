;13.
;a)Sa se intercaleze un element pe pozitia a n-a a unei liste liniare.
(defun intercaleze (l n a)
    (cond
    ((null l)nil)
    ((= n 1) (append (list a (car l)) (intercaleze(cdr l) (- n 1) a)))
    (t (cons (car l) (intercaleze (cdr l) (- n 1) a)))
    )
)    
;d.Sa se scrie o functie care testeaza egalitatea a doua multimi, fara sa se faca apel la diferenta a doua multimi.

