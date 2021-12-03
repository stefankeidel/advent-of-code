(setq input (s-lines (s-chomp (f-read "input.txt"))))

(defun baz(acc it)
  (push (substring it 0 1) acc)
  )

(defun binary-add(acc it)
  (+ acc (string-to-number it 2))
  )

(setq result (-reduce-from 'baz nil input))
(setq result2 (-reduce-from 'binary-add #b0 result))
(setq derp (cl-oddp result2))
