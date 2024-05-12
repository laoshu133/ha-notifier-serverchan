[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)

# ha-notifier-serverchan
A HA custom notification / notify powered by ServerChan.

> Inspired by [manish-custom-notifier](https://github.com/t0mer/manish-custom-notifier)

## Getting started

1. Register a [ServerChan](https://sct.ftqq.com/)
2. Get a [SendKey](https://sct.ftqq.com/sendkey)
3. Configuration


### Configuration
To use the custom notification, we need to add some linse to the configuration.yaml file.

```yaml
notify:
  - platform: manish
    name: MaNish whatsapp notifire
    target: # WhatsApp number for notificatin (Without the + sign of the country_code)
    token: #T he token for the Whatsapp cloud API
    phone_number_id: #Phone number id from the Whatsapp cloud API
    template: # Template's name's to use
    language: # Template's language
```

Restart HomeAssistant and you should see a new service :
TODO: screenshots
