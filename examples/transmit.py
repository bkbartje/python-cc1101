import logging
import time

import cc1101


logging.basicConfig(level=logging.INFO)

with cc1101.CC1101() as transceiver:
    print("defaults:", transceiver)
    transceiver.set_base_frequency_hertz(433.5e6)
    transceiver.set_symbol_rate_baud(600)
    print(transceiver)
    print("state", transceiver.get_marc_state().name)
    print("base frequency", transceiver.get_base_frequency_hertz(), "Hz")
    print("symbol rate", transceiver.get_symbol_rate_baud(), "Baud")
    print("modulation format", transceiver.get_modulation_format().name)
    print("starting transmission")
    while True:
        transceiver.transmit(list(range(1, 32)))
        time.sleep(2.0)