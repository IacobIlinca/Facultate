;10.Se da un arbore de tipul (2). Sa se precizeze nivelul pe care apare un nod x in arbore. Nivelul radacii se considera a fi 0.

(defun nivel (l x)
    (cond
    ((null l) -100)
    ((equal (car l) x) 0)
    (t (max (+ 1 ( nivel (cadr l) x)) (+ 1 (nivel (caddr l) x))))
    )
)    