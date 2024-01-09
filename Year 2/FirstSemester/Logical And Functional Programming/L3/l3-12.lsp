;12. Definiti o functie care inlocuieste un nod cu altul intr-un arbore n-ar reprezentat sub forma (radacina lista_noduri_subarb1...lista_noduri_subarbn).
;Ex: arborelele este (a (b (c)) (d) (e (f)))  si nodul 'b se inlocuieste cu nodul 'g => arborele (a (g (c)) (d) (e (f))).

(defun substituie(l e1 e2)
;l-lista initiala
;e1-elementul pe care dorim sa il inlocuim
;e2-elementul cu care vrem sa il inlocuim
	(cond
		( ( null l ) nil )
		( (equal l e1 )  e2 )
		( ( atom l )  l )
		( t  ( apply #'list ( mapcar #' ( lambda(l) 
                                            ( substituie l e1 e2 )
                                        )
                                        l 
                            ) 
              ) 
        )
	)
)

;(substituie '(A (B (C)) (D) (E (F))) 'B 'G)