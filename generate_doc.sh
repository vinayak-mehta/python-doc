#!/usr/bin/env bash

mkdir -p data/3.9/
mkdir -p data/3.8/
mkdir -p data/3.7/
mkdir -p data/3.6/

if [ -d "$DIR" ]; then
    git clone git@github.com:python/cpython
    cd cpython/Doc
else
    cd cpython/Doc
    git pull
fi

rm -rf build/html

git checkout 3.9
make html
cp -r build/html/* ../../data/3.9/
rm -rf build/html

git checkout 3.8
make html
cp -r build/html/* ../../data/3.8/
rm -rf build/html

git checkout 3.7
make html
cp -r build/html/* ../../data/3.7/
rm -rf build/html

git checkout 3.6
make html
cp -r build/html/* ../../data/3.6/
rm -rf build/html
