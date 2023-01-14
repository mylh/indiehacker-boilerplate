;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((nil
  (pylint-command . "docker exec -it {{ project_name }}_web /home/user/app/docker-pylint.sh")
  (python-shell-interpreter . "{{ project_directory }}/run_python.sh")
  (flycheck-python-pylint-executable . "{{ project_directory }}/run_pylint.sh")
  (flycheck-javascript-eslint-executable . "{{ project_directory }}/run_eslint.sh")
  (sgml-basic-offset . 2)
  (fill-column . 79)))
