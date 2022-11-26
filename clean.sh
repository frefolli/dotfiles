#!/bin/bash

rm -rf $(find . -type d | grep __pycache__)
rm -rf coverage.xml .coverage
rm -rf .scannerwork
