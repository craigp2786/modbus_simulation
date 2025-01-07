#!/usr/bin/env python3
"""
Main entry point for the Modbus Simulation Application
"""

import argparse
import threading
import logging
from modbus_sim.data_store import ModbusDataStore
from modbus_sim.device_identity import ModbusDeviceIdentity
from modbus_sim.server import ModbusServer
from modbus_sim.flask_app import ModbusFlaskApp
from modbus_sim.log_handler import InMemoryLogHandler

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger("pymodbus")


def main():
    parser = argparse.ArgumentParser(description="Modbus simulator")
    parser.add_argument("--interval", type=int, default=60, help="Interval for register updates (seconds)")
    args = parser.parse_args()

    # Create data store and device identity
    data_store = ModbusDataStore()
    device_identity = ModbusDeviceIdentity()

    # Start background thread to update data
    updater_thread = threading.Thread(
        target=data_store.update_data,
        args=(args.interval,),
        daemon=True
    )
    updater_thread.start()

    # Start Modbus server in a separate thread
    server = ModbusServer(data_store, device_identity)
    modbus_thread = threading.Thread(target=server.start, daemon=True)
    modbus_thread.start()

    # Start Flask app in the main thread
    flask_app = ModbusFlaskApp(data_store, args.interval, InMemoryLogHandler)
    flask_app.run()


if __name__ == "__main__":
    main()

