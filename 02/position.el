(setq input (--map (s-split " " it) (s-lines (s-chomp (f-read "input.txt")))))


(defun move-forward(it acc)
  (setq move-by (string-to-number (cl-second it)))
  (setq new-lateral (-sum (list move-by (car acc))))
  (list new-lateral (cl-second acc)))


(defun move-backward(it acc)
  (setq move-by (- (string-to-number (cl-second it))))
  (setq new-lateral (-sum (list move-by (car acc))))
  (list new-lateral (cl-second acc)))

(defun move-up(it acc)
  (setq move-by (- (string-to-number (cl-second it))))
  (setq new-depth (-sum (list move-by (cl-second acc))))
  (list (car acc) new-depth))

(defun move-down(it acc)
  (setq move-by (string-to-number (cl-second it)))
  (setq new-depth (-sum (list move-by (cl-second acc))))
  (list (car acc) new-depth))

(defun foo(acc it)
  (cond ((string= (car it) "forward") (move-forward it acc))
        ((string= (car it) "backward") (move-backward it acc))
        ((string= (car it) "up") (move-up it acc))
        ((string= (car it) "down") (move-down it acc))
        )
  )

(setq result (-reduce-from
              'foo
              '(0 0) input))

(message "%d " (-product  result))
