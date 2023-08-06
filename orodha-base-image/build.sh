#!/bin/bash
while getopts :t:l:u:p: flag
do
	case "${flag}" in
		t) BUILD_TAG=${OPTARG};;
		l) LAUNCH_OPTION=${OPTARG};;
		u) DOCKER_USERNAME=${OPTARG};;
		p) DOCKER_PASSWORD=${OPTARG};;
	esac
done

if [ -z "$BUILD_TAG" ];
  then
    echo "\$BUILD_TAG is not defined, defaulting to 'latest'"
	BUILD_TAG=latest
fi

if [ -z "$LAUNCH_OPTION" ];
  then
    echo "\$LAUNCH_OPTION is not defined, defaulting to 'prod'"
    LAUNCH_OPTION=prod
fi

if [ "$LAUNCH_OPTION" != "prod" ] && [ "$LAUNCH_OPTION" != "dev" ];
  then
    echo "\$LAUNCH_OPTION can only be set to 'dev' or 'prod', was set to ${LAUNCH_OPTION}, cannot complete build."
	exit 1
fi

if [ -z "$DOCKER_USERNAME" ];
  then
    echo "\$DOCKER_USERNAME is not defined, cannot complete build."
	exit 1
fi

if [ -z "$DOCKER_PASSWORD" ];
  then
    echo "\$DOCKER_PASSWORD is not defined, cannot complete build."
	exit 1
fi

export TAG=edisonstuart/orodha-base-image-${LAUNCH_OPTION}/${BUILD_TAG}


docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD

docker build --build-arg REQUIREMENTS_FILE=${LAUNCH_OPTION}-requirements.txt -t ${TAG} .

docker push $TAG
