# osdp_example.py

from osdp import SerialPortOsdpConnection
from osdp import ControlPanel

# Create an OSDP connection with a specific serial port and baud rate
conn = SerialPortOsdpConnection(port='/dev/tty.wchusbserial1420', baud_rate=9600)

# Create an OSDP control panel
cp = ControlPanel()

# Start the connection and get the bus ID
bus_id = cp.start_connection(conn)

# Add an OSDP device to the control panel
cp.add_device(connection_id=bus_id, address=0x7F, use_crc=True, use_secure_channel=False)

# Retrieve the ID report from the OSDP device
id_report = cp.id_report(connection_id=bus_id, address=0x7F)

# Retrieve the device capabilities
device_capabilities = cp.device_capabilities(connection_id=bus_id, address=0x7F)

# Retrieve the local status of the OSDP device
local_status = cp.local_status(connection_id=bus_id, address=0x7F)

# Retrieve the input status of the OSDP device
input_status = cp.input_status(connection_id=bus_id, address=0x7F)

# Retrieve the output status of the OSDP device
output_status = cp.output_status(connection_id=bus_id, address=0x7F)

# Shutdown the OSDP connection
cp.shutdown()
