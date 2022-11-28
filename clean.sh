#!/bin/bash

rm -rf $(find . -type d | grep __pycache__)
rm -rf coverage.xml .coverage htmlcov
rm -rf .scannerwork
