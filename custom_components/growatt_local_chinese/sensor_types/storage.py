"""Growatt Sensor definitions for the Inverter type."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    UnitOfEnergy,
    UnitOfPower,
    PERCENTAGE,
)
from .sensor_entity_description import GrowattSensorEntityDescription
from .switch_entity_description import GrowattSwitchEntityDescription

from ..API.device_type.base import (
    ATTR_AC_CHARGE_ENABLED,
    ATTR_SOC_PERCENTAGE,
    ATTR_DISCHARGE_POWER,
    ATTR_CHARGE_POWER,
    ATTR_ENERGY_TO_USER_TODAY,
    ATTR_ENERGY_TO_USER_TOTAL,
    ATTR_ENERGY_TO_GRID_TODAY,
    ATTR_ENERGY_TO_GRID_TOTAL,
    ATTR_DISCHARGE_ENERGY_TODAY,
    ATTR_DISCHARGE_ENERGY_TOTAL,
    ATTR_CHARGE_ENERGY_TODAY,
    ATTR_CHARGE_ENERGY_TOTAL,
    ATTR_PAC_TO_GRID_TOTAL,
    ATTR_PAC_TO_USER_TOTAL,
)

STORAGE_SWITCH_TYPES: tuple[GrowattSwitchEntityDescription, ...] = (
    GrowattSwitchEntityDescription(
        key=ATTR_AC_CHARGE_ENABLED,
        name="AC充电",
        state_on=0x1,
        state_off=0x0
    ),
)


STORAGE_SENSOR_TYPES: tuple[GrowattSensorEntityDescription, ...] = (
    GrowattSensorEntityDescription(
        key=ATTR_SOC_PERCENTAGE,
        name="SOC电量百分比",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY
    ),
    GrowattSensorEntityDescription(
        key=ATTR_DISCHARGE_POWER,
        name="放电功率",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER
    ),
    GrowattSensorEntityDescription(
        key=ATTR_CHARGE_POWER,
        name="充电功率",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER
    ),
    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_GRID_TOTAL,
        name="输出到电网总量",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_GRID_TODAY,
        name="今日输出到电网",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_USER_TOTAL,
        name="输出到用户总量",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),

    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_USER_TODAY,
        name="今日输出到用户",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_AC_CHARGE_ENABLED,
        name="AC充电已启用"
    ),
    GrowattSensorEntityDescription(
        key=ATTR_DISCHARGE_ENERGY_TODAY,
        name="今日电池放电量",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_DISCHARGE_ENERGY_TOTAL,
        name="电池总放电量",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_CHARGE_ENERGY_TODAY,
        name="今日电池充电量",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_CHARGE_ENERGY_TOTAL,
        name="电池总充电量",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_PAC_TO_USER_TOTAL,
        name="AC输出到用户总量",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_PAC_TO_GRID_TOTAL,
        name="AC输出到电网总量",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
)
