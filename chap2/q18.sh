#!/bin/bash
cat ./popular-names.txt | sort -n -r -k 3 > ./sorted.txt