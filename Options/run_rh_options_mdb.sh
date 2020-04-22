#!/usr/bin/env sh

echo $(date +"%D %T") ' starting rh_options_mdb'

cd /Users/philipmassey/PycharmProjects/Options/
python3 rh_options_mdb.py NET
python3 rh_options_mdb.py FSLY
python3 rh_options_mdb.py CRWD
python3 rh_options_mdb.py APHA
python3 rh_options_mdb.py SDGR

echo $(date +"%D %T") ' completed rh_options_mdb'

