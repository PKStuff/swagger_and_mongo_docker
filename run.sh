#!/bin/bash -e

pushd src

docker-compose -f local-compose.yml down

docker-compose -f local-compose.yml up

popd