FROM python:3.11.4-alpine3.18

ARG REQUIREMENTS_FILE
RUN mkdir -p /requirements
COPY ./${REQUIREMENTS_FILE} ./requirements

RUN apk update && \
	apk add python3 && \
	pip install -r requirements/${REQUIREMENTS_FILE} && \
	pip install orodha-keycloak && \
	rm -r requirements
