;13.Se da un arbore de tipul (2). Sa se afiseze calea de la radacina pana la un nod x dat.

(defun exista (arb e)
    (cond 
    ((null arb) nil)
    ((equal (car arb) e) t)
    (t (or (exista (cadr arb) e) (exista (caddr arb) e)))
    )
)

(defun cale (e arb)
    (cond
    ((null arb)nil)
    ((equal(car arb) e) (list e))
    ((exista (cadr arb) e) (cons (car arb) (cale e (cadr arb))))
    ((exista (caddr arb) e) (cons (car arb) (cale e (caddr arb))))
    (t nil)
    )
)