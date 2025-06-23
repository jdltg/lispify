#!/bin/bash

BASE_URL="http://localhost:8080/execute"

echo "Test 1: Simple arithmetic"
curl --silent --get --data-urlencode "code=(+ 1 2)" $BASE_URL
echo -e "\nExpected: 3"
echo "-----------------------------"

echo "Test 2: Define a variable"
curl --silent --get --data-urlencode "code=(defparameter x 42)" $BASE_URL
echo -e "\nExpected: X"
echo "-----------------------------"

echo "Test 3: Use the variable"
curl --silent --get --data-urlencode "code=x" $BASE_URL
echo -e "\nExpected: 42"
echo "-----------------------------"

echo "Test 4: Error case"
curl --silent --get --data-urlencode "code=(+ 1 'a)" $BASE_URL
echo -e "\nExpected: Error or NIL"
echo "-----------------------------"

echo "Test 5: Multiline expression"
curl --silent --get --data-urlencode "code=(progn (defparameter y 100) (* y 2))" $BASE_URL
echo -e "\nExpected: 200"
echo "-----------------------------"
