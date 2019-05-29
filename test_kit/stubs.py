#!/usr/bin/env python3
# -------------------------------------------------------------------------------------------------
# <copyright file="stubs.py" company="Invariance Pte">
#  Copyright (C) 2018-2019 Invariance Pte. All rights reserved.
#  The use of this source code is governed by the license as found in the LICENSE.md file.
#  http://www.invariance.com
# </copyright>
# -------------------------------------------------------------------------------------------------

from decimal import Decimal
from datetime import datetime, timedelta, timezone

from inv_trader.model.enums import Venue, Resolution, QuoteType, Currency, SecurityType
from inv_trader.model.objects import Quantity, Symbol, Price, BarSpecification, BarType, Bar, Instrument
from inv_trader.model.identifiers import InstrumentId

# Unix epoch is the UTC time at 00:00:00 on 1/1/1970
UNIX_EPOCH = datetime(1970, 1, 1, 0, 0, 0, 0, timezone.utc)
AUDUSD_FXCM = Symbol('AUDUSD', Venue.FXCM)
GBPUSD_FXCM = Symbol('GBPUSD', Venue.FXCM)
USDJPY_FXCM = Symbol('USDJPY', Venue.FXCM)
ONE_MINUTE_BID = BarSpecification(1, Resolution.MINUTE, QuoteType.BID)
ONE_MINUTE_ASK = BarSpecification(1, Resolution.MINUTE, QuoteType.ASK)
ONE_MINUTE_MID = BarSpecification(1, Resolution.MINUTE, QuoteType.MID)
ONE_SECOND_MID = BarSpecification(1, Resolution.SECOND, QuoteType.MID)


class TestStubs:

    @staticmethod
    def unix_epoch(offset_mins: int=0) -> datetime:
        """
        Generate a stub datetime based on the given offset from Unix epoch time.

        Unix time (also known as POSIX time or epoch time) is a system for
        describing instants in time, defined as the number of seconds that have
        elapsed since 00:00:00 Coordinated Universal Time (UTC), on Thursday,
        1 January 1970, minus the number of leap seconds which have taken place
        since then.

        :return: The unix epoch datetime plus any offset.
        """
        return UNIX_EPOCH + timedelta(minutes=offset_mins)

    @staticmethod
    def instrument_gbpusd():
        return Instrument(
            InstrumentId('GBPUSD.FXCM'),
            Symbol('GBPUSD', Venue.FXCM),
            'GBP/USD',
            Currency.USD,
            SecurityType.FOREX,
            tick_precision=5,
            tick_size=Decimal('0.00001'),
            round_lot_size=Quantity(1000),
            min_stop_distance_entry=0,
            min_limit_distance_entry=0,
            min_stop_distance=0,
            min_limit_distance=0,
            min_trade_size=Quantity(1),
            max_trade_size=Quantity(50000000),
            rollover_interest_buy=Decimal(),
            rollover_interest_sell=Decimal(),
            timestamp=UNIX_EPOCH)

    @staticmethod
    def instrument_usdjpy():
        return Instrument(
            InstrumentId('USDJPY.FXCM'),
            Symbol('USDJPY', Venue.FXCM),
            'USD/JPY',
            Currency.JPY,
            SecurityType.FOREX,
            tick_precision=3,
            tick_size=Decimal('0.001'),
            round_lot_size=Quantity(1000),
            min_stop_distance_entry=Decimal(),
            min_limit_distance_entry=Decimal(),
            min_stop_distance=Decimal(),
            min_limit_distance=Decimal(),
            min_trade_size=Quantity(1),
            max_trade_size=Quantity(50000000),
            rollover_interest_buy=Decimal(),
            rollover_interest_sell=Decimal(),
            timestamp=UNIX_EPOCH)

    @staticmethod
    def bartype_audusd_1min_bid():
        return BarType(AUDUSD_FXCM, ONE_MINUTE_BID)

    @staticmethod
    def bartype_audusd_1min_ask():
        return BarType(AUDUSD_FXCM, ONE_MINUTE_ASK)

    @staticmethod
    def bartype_gbpusd_1min_bid():
        return BarType(GBPUSD_FXCM, ONE_MINUTE_BID)

    @staticmethod
    def bartype_gbpusd_1min_ask():
        return BarType(GBPUSD_FXCM, ONE_MINUTE_ASK)

    @staticmethod
    def bartype_gbpusd_1sec_mid():
        return BarType(GBPUSD_FXCM, ONE_SECOND_MID)

    @staticmethod
    def bartype_usdjpy_1min_bid():
        return BarType(USDJPY_FXCM, ONE_MINUTE_BID)

    @staticmethod
    def bartype_usdjpy_1min_ask():
        return BarType(USDJPY_FXCM, ONE_MINUTE_ASK)

    @staticmethod
    def bar_5decimal():
        return Bar(Price('1.00002'),
                   Price('1.00004'),
                   Price('1.00001'),
                   Price('1.00003'),
                   100000,
                   UNIX_EPOCH)

    @staticmethod
    def bar_3decimal():
        return Bar(Price('90.002'),
                   Price('90.004'),
                   Price('90.001'),
                   Price('90.003'),
                   100000,
                   UNIX_EPOCH)
