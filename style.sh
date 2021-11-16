#!/bin/bash
cd src
isort .
black .
cd ..
./bin/code-analysis