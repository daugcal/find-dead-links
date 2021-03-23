INSTALL_DIR = ~/bin
BASH_SCRIPT = ${INSTALL_DIR}/find-dead-links
PY_SCRIPT = ${INSTALL_DIR}/find-dead-links.py
VENV = ${INSTALL_DIR}/badLinksEnv

install: ${BASH_SCRIPT} ${PY_SCRIPT} ${VENV}

${BASH_SCRIPT}: find-dead-links
	cp find-dead-links ${INSTALL_DIR}
	chmod 700 ${BASH_SCRIPT}

${PY_SCRIPT}: find-dead-links.py
	cp find-dead-links.py ${INSTALL_DIR} 
	chmod 700 ${BASH_SCRIPT}

${VENV}:
	virtualenv -p python3 ${VENV}
	source ${VENV}/bin/activate && pip install requests && pip install beautifulsoup4
