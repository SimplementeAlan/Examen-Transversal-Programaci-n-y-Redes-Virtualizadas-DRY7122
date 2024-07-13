from ncclient import manager

# Conectar al router CSR1000v
m = manager.connect(
    host="192.168.1.7",  # Cambia esto por la IP de tu router
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)
# Cambiar el nombre del router
config_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>ArratiaNavarreteAvila</hostname>
    </native>
</config>
"""
m.edit_config(target="running", config=config_data)

# Crear la interfaz loopback 11
config_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>11</name>
                <ip>
                    <address>
                        <primary>
                            <address>11.11.11.11</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
m.edit_config(target="running", config=config_data)

# Cerrar la conexión
m.close_session()

