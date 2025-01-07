# Modbus Simulation Script

This Python application simulates a Modbus TCP server and displays register values in a Flask web interface.

## Features

- **Asynchronous** Modbus TCP server (using `StartAsyncTcpServer`)
- **Background data updates** for simulated sensors and thermostats
- **Flask** interface showing current register values and logs
- **In-memory log handler** to capture logs for web display

## Requirements

- Python 3.9+ (recommended)
- `pymodbus 3.8.3`
- `Flask`

Install via:

```bash
pip install -r requirements.txt

