#!/usr/bin/env python3
# -------------------------------------------------------------------------------------------------
# <copyright file="resolution.pxd" company="Invariance Pte">
#  Copyright (C) 2018-2019 Invariance Pte. All rights reserved.
#  The use of this source code is governed by the license as found in the LICENSE.md file.
#  http://www.invariance.com
# </copyright>
# -------------------------------------------------------------------------------------------------

# cython: language_level=3, boundscheck=False, wraparound=False, nonecheck=False


cpdef enum Resolution:
    UNKNOWN = -1,
    TICK = 0,
    SECOND = 1,
    MINUTE = 2,
    HOUR = 3,
    DAY = 4

cdef inline str resolution_string(int value):
    if value == 0:
        return "TICK"
    elif value == 1:
        return "SECOND"
    elif value == 2:
        return "MINUTE"
    elif value == 3:
        return "HOUR"
    elif value == 4:
        return "DAY"
    elif value == -1:
        return "UNKNOWN"
    else:
        return "UNKNOWN"