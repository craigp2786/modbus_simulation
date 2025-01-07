import asyncio
import logging
from pymodbus.server import StartAsyncTcpServer
from pymodbus.framer import FramerSocket

logger = logging.getLogger("pymodbus")


class ModbusServer:
    def __init__(self, data_store, device_identity):
        self.data_store = data_store
        self.device_identity = device_identity

    async def start_async_server(self):
        """
        Asynchronous start for the Modbus TCP Server.
        """
        logger.info("Starting Modbus TCP Server on 0.0.0.0:5020")
        await StartAsyncTcpServer(
            context=self.data_store.context,
            identity=self.device_identity.identity,
            address=("0.0.0.0", 5020),
            framer="socket",
        )

    def start(self):
        """
        Start the Modbus TCP Server in a dedicated asyncio event loop.
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.start_async_server())
        loop.run_forever()
