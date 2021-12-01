(defun parse-data (f)
  (with-temp-buffer
    (insert-file-contents f)
    (buffer-substring-no-properties
     (point-min)
     (point-max))))

(defvar puzzle-input)
(setq puzzle-input (split-string
                    (parse-data "data_puzzle_1.txt") "\n" t))

(defvar reduced-input)
(setq reduced-input (mapcar '-sum (-partition-in-steps 3 1 (mapcar 'string-to-number puzzle-input))))

(defun count-increases(depths)
  (let ((counter 0) (cur) (prev -1))
    (while depths
      (setq cur (car depths))
      (if (/=  prev -1)
          (if (> cur prev)
              (setq counter (+ counter 1)))
          )
      (setq prev cur)
      (setq depths (cdr depths))
      )
    counter)
  )

(message "%d " (count-increases reduced-input))
