PACKAGE_NAME_PREFIX := 'embert-models-'
WHEEL_PREFIX := $(shell echo ${PACKAGE_NAME_PREFIX} | tr '-' '_')

all:
	@echo "See Makefile for possible targets and supply model name with MODEL_NAME variable!"

check-model_name:
ifndef MODEL_NAME
	$(error MODEL_NAME is undefined)
endif

build: check-model_name
	echo ${MODEL_NAME} > model_name.txt
	@echo "Building package..."
	python3 setup.py sdist bdist_wheel

install-user: check-model_name build
	@echo "Installing package to user..."
	pip3 install dist/${WHEEL_PREFIX}${MODEL_NAME}*.whl

uninstall: check-model_name
	@echo "Uninstalling..."
	pip3 uninstall -y ${PACKAGE_NAME_PREFIX}${MODEL_NAME}

clean: check-model_name
	rm -rf dist/ build/ ${PACKAGE_NAME_PREFIX}${MODEL_NAME}.egg-info/ model_name.txt MANIFEST.in
