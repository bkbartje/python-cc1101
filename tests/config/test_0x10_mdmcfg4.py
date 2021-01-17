# python-cc1101 - Python Library to Transmit RF Signals via CC1101 Transceivers
#
# Copyright (C) 2020 Fabian Peter Hammerle <fabian@hammerle.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import unittest.mock

import pytest

# pylint: disable=protected-access


@pytest.mark.parametrize(
    ("mdmcfg4", "exponent"),
    (
        (0b10001100, 12),
        (0b10001001, 9),
        (0b10001111, 15),
        (0b10000000, 0),
        (0b10111100, 12),
        (0b10111111, 15),
        (0b10110000, 0),
    ),
)
def test__get_symbol_rate_exponent(transceiver, mdmcfg4, exponent):
    transceiver._spi.xfer.return_value = [15, mdmcfg4]
    assert transceiver._get_symbol_rate_exponent() == exponent
    transceiver._spi.xfer.assert_called_once_with([0x10 | 0x80, 0])


@pytest.mark.parametrize(
    ("mdmcfg4_before", "mdmcfg4_after", "exponent"),
    (
        (0b10001100, 0b10001100, 12),
        (0b10001100, 0b10001111, 15),
        (0b10001100, 0b10000000, 0),
        (0b10001100, 0b10001010, 0b1010),
        (0b01111100, 0b01111100, 12),
        (0b01111100, 0b01111111, 15),
        (0b01111100, 0b01110000, 0),
        (0b01110001, 0b01111100, 12),
    ),
)
def test__set_symbol_rate_exponent(
    transceiver, mdmcfg4_before, mdmcfg4_after, exponent
):
    transceiver._spi.xfer.return_value = [0x0F, 0x0F]
    with unittest.mock.patch.object(
        transceiver, "_read_single_byte", return_value=mdmcfg4_before
    ):
        transceiver._set_symbol_rate_exponent(exponent)
    transceiver._spi.xfer.assert_called_once_with([0x10 | 0x40, mdmcfg4_after])
