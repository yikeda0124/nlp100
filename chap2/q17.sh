#!/bin/bash
cut -f 1 ./popular-names.txt | sort | uniq | wc -l