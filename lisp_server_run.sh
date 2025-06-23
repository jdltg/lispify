#!/bin/bash

sbcl --load server.lisp --eval "(lisp-server:start-server)"

