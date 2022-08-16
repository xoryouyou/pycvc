# -*- coding: utf-8 -*-
"""
/* 
 * This file is part of the pyCVC distribution (https://github.com/polhenarejos/pycvc).
 * Copyright (c) 2022 Pol Henarejos.
 * 
 * This program is free software: you can redistribute it and/or modify  
 * it under the terms of the GNU General Public License as published by  
 * the Free Software Foundation, version 3.
 *
 * This program is distributed in the hope that it will be useful, but 
 * WITHOUT ANY WARRANTY; without even the implied warranty of 
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License 
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */
"""

import oid

def to_bytes(n):
    if (n == 0):
        return bytearray([0])
    if (isinstance(n, int)):
        return bytearray(n.to_bytes((n.bit_length() + 7) // 8, 'big'))
    return n #Assume is already 

def bcd(s):
    return bytearray([int(c) for c in s])

def scheme_rsa(o):
    return (o == oid.ID_TA_RSA_V1_5_SHA_1 or o == oid.ID_TA_RSA_V1_5_SHA_256 or o == oid.ID_TA_RSA_V1_5_SHA_512 or
        o == oid.ID_TA_RSA_PSS_SHA_1 or o == oid.ID_TA_RSA_PSS_SHA_256 or o == oid.ID_TA_RSA_PSS_SHA_512)

def scheme_ecdsa(o):
    return (o == oid.ID_TA_ECDSA_SHA_1 or o == oid.ID_TA_ECDSA_SHA_224 or o == oid.ID_TA_ECDSA_SHA_256 or 
            o == oid.ID_TA_ECDSA_SHA_384 or o == oid.ID_TA_ECDSA_SHA_512)

def from_bcd(c):
    return ''.join([str(s) for s in c])