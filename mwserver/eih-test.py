#!/usr/bin/env python

import yaml

from fitbit_client import FitbitClient

with open("/home/eric/creds/fitbit.yaml", 'r') as f:
    try:
        creds = yaml.load(f)
    except yaml.YAMLError as e:
        print(e)
        exit

EIH_USERID = creds['eih_userid']
EIH_TOKEN = creds['eih_token']
MPE_USERID = creds['mpe_userid']
MPE_TOKEN = creds['mpe_token']

fbc = FitbitClient()

eih = fbc.get_measurements(EIH_USERID, EIH_TOKEN)
mpe = fbc.get_measurements(MPE_USERID, MPE_TOKEN)

print eih
print
print mpe
