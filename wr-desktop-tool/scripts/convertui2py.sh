#!/bin/bash
pwd
echo "Generate python file from qt Interface"
pyuic4 -x qt_guis/frontend.ui  -o python/frontend.py 
chmod u+x python/frontend.py
echo "frontend.py generated in python/ folder"

