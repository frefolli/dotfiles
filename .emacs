;;;; -*- Mode:Lisp -*-

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(custom-enabled-themes '(misterioso))
 '(inhibit-startup-screen t))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
;; custom-set-faces was added by Custom.
;; If you edit it by hand, you could mess it up, so be careful.
;; Your init file should contain only one such instance.
;; If there is more than one, they won't work right.

;; define wrap 80 columns for langs
(defun symbol-join (symbola symbolb)
  (car
   (read-from-string
    (concat
     (symbol-name symbola)
     (symbol-name symbolb)))))
(defun craft-hook (lang)
  (symbol-join lang '-mode-hook))
(defun antonhook (lang)
  (let ((hook (craft-hook lang)))
    (and
     (add-hook hook 'turn-on-auto-fill)
     (add-hook hook (lambda () (set-fill-column 80))))))
(defun antonlook (llangs)
  (if (null llangs) t
    (and
     (antonhook (car llangs))
     (antonlook (cdr llangs)))))
;; set wraps
(defvar list-of-programming-languages
  (list 'prolog 'lisp 'c 'java 'c++ 'python))
(antonlook list-of-programming-languages)

(global-set-key (kbd "<f7>") 'display-fill-column-indicator-mode)
(global-set-key (kbd "<f6>")
		(lambda ()
		  (interactive)
		  (mark-whole-buffer)
		  (let
		      ((start 0)
		       (end (region-end)))
		    (indent-region start end))))

;; display a visible dot insteam of blank chars
(standard-display-ascii ?\t "····")
(standard-display-ascii ?\s "·")

;; Source: http://www.emacswiki.org/emacs-en/download/misc-cmds.el
(defun revert-buffer-no-confirm ()
    "Revert buffer without confirmation."
    (interactive)
    (revert-buffer :ignore-auto :noconfirm))
