import logging
from flask import Flask, render_template_string

logger = logging.getLogger("pymodbus")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Modbus Device Values</title>
    <style>
        body { font-family: sans-serif; margin: 40px; }
        table { border-collapse: collapse; min-width: 300px; }
        td, th { border: 1px solid #ccc; padding: 8px; }
        th { background-color: #f0f0f0; }
    </style>
</head>
<body>
<h1>Current Modbus Values (Updated every {{ interval }}s)</h1>
<table>
    <thead>
        <tr>
            <th>Device</th>
            <th>Register</th>
            <th>Value</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Sensor 1</td><td>0</td><td>{{ sensor_1 }}</td></tr>
        <tr><td>Sensor 2</td><td>1</td><td>{{ sensor_2 }}</td></tr>
        <tr><td>Sensor 3</td><td>2</td><td>{{ sensor_3 }}</td></tr>
        <tr><td>Thermostat 1</td><td>3</td><td>{{ thermostat_1 }}</td></tr>
        <tr><td>Thermostat 2</td><td>4</td><td>{{ thermostat_2 }}</td></tr>
        <tr><td>Fluid Level Monitor</td><td>5</td><td>{{ fluid_level }}</td></tr>
    </tbody>
</table>
<h2>Log Output</h2>
<pre>{{ logs }}</pre>
</body>
</html>
"""


class ModbusFlaskApp:
    def __init__(self, data_store, update_interval, log_handler_class):
        from .log_handler import InMemoryLogHandler  # or direct import if needed

        self.app = Flask(__name__)
        self.data_store = data_store
        self.update_interval = update_interval
        self.log_storage = []

        # Configure logging for in-memory capture
        handler = log_handler_class(self.log_storage)
        logger.addHandler(handler)

        @self.app.route("/")
        def index():
            # Fetch register values
            sensor_1 = self.data_store.store.getValues(3, 0, count=1)[0]
            sensor_2 = self.data_store.store.getValues(3, 1, count=1)[0]
            sensor_3 = self.data_store.store.getValues(3, 2, count=1)[0]
            thermostat_1 = self.data_store.store.getValues(3, 3, count=1)[0]
            thermostat_2 = self.data_store.store.getValues(3, 4, count=1)[0]
            fluid_level = self.data_store.store.getValues(3, 5, count=1)[0]
            logs = "\n".join(self.log_storage[-50:])

            return render_template_string(
                HTML_TEMPLATE,
                sensor_1=sensor_1,
                sensor_2=sensor_2,
                sensor_3=sensor_3,
                thermostat_1=thermostat_1,
                thermostat_2=thermostat_2,
                fluid_level=fluid_level,
                logs=logs,
                interval=self.update_interval,
            )

    def run(self):
        """
        Start the Flask web server.
        """
        self.app.run(host="0.0.0.0", port=5001, debug=True, use_reloader=False)

