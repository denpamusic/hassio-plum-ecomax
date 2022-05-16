"""Constants for Plum ecoMAX test suite."""

from custom_components.plum_ecomax.const import (
    CONF_CAPABILITIES,
    CONF_CONNECTION_TYPE,
    CONF_DEVICE,
    CONF_HOST,
    CONF_MODEL,
    CONF_PORT,
    CONF_SOFTWARE,
    CONF_UID,
    CONF_UPDATE_INTERVAL,
    CONNECTION_TYPE_SERIAL,
    CONNECTION_TYPE_TCP,
)

# Config entry data for TCP connection.
MOCK_CONFIG_DATA = {
    CONF_CONNECTION_TYPE: CONNECTION_TYPE_TCP,
    CONF_DEVICE: "/dev/ttyUSB0",
    CONF_HOST: "example.com",
    CONF_PORT: 8899,
    CONF_UPDATE_INTERVAL: 10,
}

# Config entry data for serial connection.
MOCK_CONFIG_DATA_SERIAL = {
    CONF_CONNECTION_TYPE: CONNECTION_TYPE_SERIAL,
    CONF_DEVICE: "/dev/ttyUSB0",
    CONF_PORT: 8899,
    CONF_UPDATE_INTERVAL: 10,
}

# Device data that added on entry create.
MOCK_DEVICE_DATA = {
    CONF_UID: "D251PAKR3GCPZ1K8G05G0",
    CONF_MODEL: "EM350P2",
    CONF_SOFTWARE: "1.13.5.Z1",
    CONF_CAPABILITIES: ["fuel_burned", "heating_temp"],
}
