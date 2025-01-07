import time
import random
import logging
from pymodbus.datastore import (
    ModbusSlaveContext,
    ModbusServerContext,
    ModbusSequentialDataBlock
)

logger = logging.getLogger("pymodbus")


class ModbusDataStore:
    def __init__(self):
        """
        Creates the Modbus data store (holding registers, etc.).
        """
        self.store = ModbusSlaveContext(
            hr=ModbusSequentialDataBlock(0, [0] * 10)
        )
        self.context = ModbusServerContext(slaves=self.store, single=True)

    def update_data(self, interval):
        """
        Periodically updates the simulated registers.
        """
        while True:
            # Example data updates
            self.store.setValues(3, 0, [random.randint(0, 100)])  # Sensor 1
            self.store.setValues(3, 1, [random.randint(0, 100)])  # Sensor 2
            self.store.setValues(3, 2, [random.randint(0, 100)])  # Sensor 3
            self.store.setValues(3, 3, [random.randint(15, 30)])  # Thermostat 1
            self.store.setValues(3, 4, [random.randint(15, 30)])  # Thermostat 2
            self.store.setValues(3, 5, [random.randint(0, 100)])  # Fluid Level

            time.sleep(interval)

