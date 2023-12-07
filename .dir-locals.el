;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((nil
  (pylint-command . "{{ project_directory }}/emacs_docker_integration/docker_pylint_command.sh")
  (python-shell-interpreter . "{{ project_directory }}/emacs_docker_integration/run_python.sh")
  (flycheck-python-pylint-executable . "{{ project_directory }}/emacs_docker_integration/run_pylint.sh")
  (flycheck-javascript-eslint-executable . "{{ project_directory }}/emacs_docker_integration/run_eslint.sh")
  (sgml-basic-offset . 2)
  (fill-column . 79)))
