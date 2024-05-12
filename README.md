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
  - platform: serverchan
    name: ServerChan notifier
    token: SC_xxx # The token of ServerChan SendKey
```

Restart HomeAssistant and you should see a new service :
TODO: screenshots
