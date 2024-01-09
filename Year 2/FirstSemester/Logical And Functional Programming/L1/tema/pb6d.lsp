;6d
(defun nratom(l)
  (cond
     ((null l) 0)
     ((atom (car l)) (+ 1 (nratom (cdr l))))
     (t (nratom (cdr l)))
  )
)
;(nratom '(12  s (3 (4 5) (6 7)) 8 (9 10) 78 ))