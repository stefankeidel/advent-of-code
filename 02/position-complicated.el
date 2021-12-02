(setq input (--map (s-split " " it) (s-lines (s-chomp (f-read "input.txt")))))


(defun move-forward(it acc)
  ; move-forward is the only way to change depth
  (setq move-by (string-to-number (cl-second it)))
  (setq new-lateral (-sum (list move-by (car acc))))

  ; depth change = aim * move-by
  (setq depth-change (-product (list (cl-third acc) move-by)))
  (setq new-depth (-sum (list depth-change (cl-second acc))))
  (list new-lateral new-depth (cl-third acc)))


(defun move-up(it acc)
  (setq move-by (- (string-to-number (cl-second it))))
  (setq new-aim (-sum (list move-by (cl-third acc))))
  (list (car acc) (cl-second acc) new-aim))

(defun move-down(it acc)
  (setq move-by (string-to-number (cl-second it)))
  (setq new-aim (-sum (list move-by (cl-third acc))))
  (list (car acc) (cl-second acc) new-aim))

(defun foo(acc it)
  (cond ((string= (car it) "forward") (move-forward it acc))
        ((string= (car it) "up") (move-up it acc))
        ((string= (car it) "down") (move-down it acc))
        )
  )

(setq result (-reduce-from
              'foo
              '(0 0 0) input))

(message "%d " (-product (list (car result) (cl-second result))))
