; Lab 13: Final Review - Optional Questions

; Q6
(define (nodots s)
  (cond ((null? s) nil)
    ((not (pair? s)) (list s))
    ((pair? (car s))
      (cons (nodots (car s)) (nodots (cdr s))))
    ((pair? s)
      (cons (car s) (nodots (cdr s)))))
)

; Q7
(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far (car curr)) #t)
          (else (pair-tracker (cons (car curr) seen-so-far) (cdr-stream curr)) ))
    )

  (pair-tracker nil s)
)

(define (contains? lst s)
  (cond
    ((null? lst) #f)
    ((eq? (car lst) s) #t)
    (else (contains? (cdr lst) s))
  )
)

; Q8
; ; scm> (switch (+ 1 1) ((1 (print 'a))
; ;                       (2 (print 'b))
; ;                       (3 (print 'c))))
; ; b
(define-macro (switch expr cases)
  `(filter (lambda x: (= (car (quote ,(car cases))) ,expr)) ,cases)

  ; `(map list ,cases)
  ; `(car (quote ,(car cases)))

; Solution #2
  ; (cons 'cond 
  ;   (map
  ;     (lambda (case)
  ;       (cons `(equal? ,expr (quote ,(car case))) (cdr case))
  ;     )
  ;     cases
  ;   )
  ; )
)

