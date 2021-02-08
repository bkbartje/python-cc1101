import unittest.mock

import cc1101


def test___str___():
    transceiver = cc1101.CC1101()
    with unittest.mock.patch.object(
        transceiver,
        "get_main_radio_control_state_machine_state",
        return_value=cc1101.MainRadioControlStateMachineState.IDLE,
    ), unittest.mock.patch.object(
        transceiver, "get_base_frequency_hertz", return_value=433.92e6
    ), unittest.mock.patch.object(
        transceiver, "get_symbol_rate_baud", return_value=2142
    ), unittest.mock.patch.object(
        transceiver,
        "get_modulation_format",
        return_value=cc1101.ModulationFormat.ASK_OOK,
    ), unittest.mock.patch.object(
        transceiver,
        "get_sync_mode",
        return_value=cc1101.SyncMode.NO_PREAMBLE_AND_SYNC_WORD,
    ), unittest.mock.patch.object(
        transceiver,
        "get_packet_length_mode",
        return_value=cc1101.PacketLengthMode.FIXED,
    ), unittest.mock.patch.object(
        transceiver, "get_packet_length_bytes", return_value=21
    ), unittest.mock.patch.object(
        transceiver, "get_output_power", return_value=(0, 0xC0)
    ):
        assert (
            str(transceiver) == "CC1101(marcstate=idle, base_frequency=433.92MHz, "
            "symbol_rate=2.14kBaud, modulation_format=ASK_OOK, "
            "sync_mode=NO_PREAMBLE_AND_SYNC_WORD, packet_length=21B, output_power=(0,0xc0))"
        )
