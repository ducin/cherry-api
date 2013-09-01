#!/bin/bash

export PYTHONPATH="$PYTHONPATH:`pwd`/src"
nosetests --nocapture
