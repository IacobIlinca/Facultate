;8.Sa se construiasca lista nodurilor unui arbore de tipul (2) parcurs in inordine.

;srd
(defun inordine (l)
    (cond
    ((null l)nil)
    (t(append (inordine (cadr l)) (cons (car l) (inordine (caddr l)))))
    )
)    