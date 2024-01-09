;9.Sa se converteasca un arbore de tipul (1) la un arbore de tipul (2).
;1->2
(defun cvrt (l)
    (cond 
    ((null l)nil)
    (( > (cadr l) 0) (list (append ( list (car l)) (cvrt (cddr l)))))
    ((= (cadr l) 0) (append (list (list(car l))) (cvrt (cddr l))))
    (t (cvrt (cddr l)))
    )
)

(defun convert (l)
        (car (cvrt l))
)