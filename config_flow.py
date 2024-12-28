import voluptuous as vol # type: ignore

from homeassistant import config_entries # type: ignore

from .const import DOMAIN



class GarminConnectConfigFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def _show_setup_form(self, errors=None):
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("Device Name"): str,
                    vol.Optional("Manufacturer"): str,
                    vol.Optional("Model"): str,
                    vol.Optional("Software Version"): str,
                    vol.Optional("Hardware Version"): str
                }
            ),
            errors=errors or {},
        )

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is None:
            return await self._show_setup_form()

        device = user_input["Device Name"]

        await self.async_set_unique_id(device)
        self._abort_if_unique_id_configured()
        
        return self.async_create_entry(title=device, data={
            "Device Name": device,
            "Manufacturer": user_input.get("Manufacturer", "Custom Device"),
            "Model": user_input.get("Model", device),
            "Software Version": user_input.get("Software Version", "1.0.0"),
            "Hardware Version": user_input.get("Hardware Version", "1.0.0")
            })