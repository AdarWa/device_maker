"""The Visonic Alarm Integration"""
from homeassistant.config_entries import ConfigEntry # type: ignore
from homeassistant.core import HomeAssistant # type: ignore
from homeassistant.helpers import device_registry as dr # type: ignore
from .const import DOMAIN
import logging

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setup a config entry."""
    device_registry = dr.async_get(hass)
    
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN,entry.entry_id)},
        manufacturer=entry.data["Manufacturer"],
        name=entry.data["Device Name"],
        model=entry.data["Model"],
        sw_version=entry.data["Software Version"],
        hw_version=entry.data["Hardware Version"],
    )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True