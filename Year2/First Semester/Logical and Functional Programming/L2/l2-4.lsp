;4.Sa se converteasca un arbore de tipul (2) la un arbore de tipul (1).
;2->1
(defun convert (l)
    (cond
    ((null l)nil)
    ((and (= (length l) 1 ) (listp (car l))) (convert (car l)))
    ((atom (car l)) (append  (list (car l) (- (length l) 1)) (convert (cdr l))))
    ;(t (append (list (first (car l)) 0) (convert (cdr l))))
    (t (append (list (caar l) 0) (convert (cdr l))))
    )
)    