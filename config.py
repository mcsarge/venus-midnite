#!/usr/bin/env python

# Name: 		config.py
# Purpose:	Configuration details Midnite Classic
# Date:		12-12-2024
# Version:	2.0
# Author:	Jan Bakuwel / YSolar NZ Ltd
# License:	GNU General Public License v3.0

VERSION				= "v2.0"
MIDNITE_INTERVAL    = 10 # seconds

MIDNITE1_IP         = "192.168.0.225"
MIDNITE1_UNIT       = 10
MIDNITE2_IP         = "192.168.0.226"
MIDNITE2_UNIT       = 11

MIDNITE_VICTRON	=  
   {
	   0:   0,   # Midnite Resting:     Victron Off
	   3:   4,   # Midnite Absorb:      Victron Absorption
	   4:   3,   # Midnite BulkMPPT:    Victron Bulk
	   5:   5,   # Midnite Float:       Victron Float
	   6:   5,   # Midnite FloatMPPT:   Victron Float
	   7:   7,   # Midnite Equalize:    Victron Equalize
	   10:  3,   # HyperVOC:            Victron Bulk - I guess
   }
