#!/usr/bin/env python

# Name:     config.py
# Purpose:  Configuration details Midnite Classic
# Date:     5-19-2026
# Version:  2.1
# Author:   Jan Bakuwel / YSolar NZ Ltd - Matt Sargent / Self
# License:  GNU General Public License v3.0

VERSION				= "v2.0"
MIDNITE_INTERVAL    = 10 # seconds

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
