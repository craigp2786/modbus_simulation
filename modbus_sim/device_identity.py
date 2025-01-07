from pymodbus.device import ModbusDeviceIdentification


class ModbusDeviceIdentity:
    def __init__(self):
        """
        Sets up the Modbus device identity (vendor name, product code, etc.).
        """
        self.identity = ModbusDeviceIdentification()
        self.identity.VendorName = "ExampleVendor"
        self.identity.ProductCode = "ModSim"
        self.identity.VendorUrl = "http://example.com"
        self.identity.ProductName = "Modbus Simulator"
        self.identity.ModelName = "ModbusSimModel"
        self.identity.MajorMinorRevision = "1.0"

