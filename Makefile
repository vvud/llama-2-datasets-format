PYTHON_VENV_DIR=venv
# install venv!
install:
	python -m venv ${PYTHON_VENV_DIR}
# format!
format:	## Run format application in virtual environment
	@ true \
	&& . ${PYTHON_VENV_DIR}/bin/activate \
	&& python app.py