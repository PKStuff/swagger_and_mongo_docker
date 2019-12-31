#!/bin/bash -e

pushd src

docker build -t sample .

popd