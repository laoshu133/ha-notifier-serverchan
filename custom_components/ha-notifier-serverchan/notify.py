"""
A HA custom notification / notify powered by ServerChan.
"""
import logging
from fake_useragent import UserAgent
import datetime
import requests
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.notify import (
    ATTR_TITLE, ATTR_MESSAGE, PLATFORM_SCHEMA, BaseNotificationService)

_LOGGER = logging.getLogger(__name__)

_API_ENDPOINT = 'http://sc.ftqq.com'

ATTR_TOKEN = 'token'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(ATTR_TOKEN): cv.string
})

def get_service(hass, config, discovery_info=None):
    """Get the custom notifier service."""
    token = config.get(ATTR_TOKEN)

    return ServerchanNotificationService(token)

class ServerchanNotificationService(BaseNotificationService):
    def __init__(self, token):
        """Initialize the service."""
        self._token = token

    def send_message(self, message="", **kwargs):
        """Send a message to the target."""
        url = '{}/{}.send'.format(_API_ENDPOINT, self._token)
        title = kwargs.get(ATTR_TITLE)

        # If title is not set, use message as title
        if not title:
            title = message
            message = ""

        if title:
            timestp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sendmessage = '{} {}'.format(timestp, message)
            payload = {'text': title, 'desp': sendmessage}
            ua = UserAgent()
            header = {'user-agent': ua.random }
            response = requests.get(url,params = payload,headers = header)
            _LOGGER.debug("sneding out message")

            if response.status_code != 200:
                obj = response.json()
                error_message = obj['error']['message']
                error_code = obj['error']['code']
                _LOGGER.error(
                    "Sending message error %s : %s (Code %s)", resp.status_code, error_message,
                    error_code)
        else:
            _LOGGER.error("Title can NOT be null")
