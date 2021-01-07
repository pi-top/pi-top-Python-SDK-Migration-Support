# pi-top Python SDK Migration Support

This repository attempts to assist users in migrating to the [pi-top Python SDK](https://github.com/pi-top/pi-top-Python-SDK/) by trying to ensure that Python and shell script code written using legacy pi-top Python libraries/CLIs continue to work using the latest SDK, whilst at the same time clearly notifying the user that they should update their code to use the new commands/Python module directly.

It is offered as a courtesy, and is not considered officially supported.
It will be deprecated and removed in the future.


### CLIs

| Legacy CLI Command | Legacy Debian Package | Superceding CLI Command     | Superceding Debian Package |
|--------------------|-----------------------|-----------------------------|----------------------------|
| `pt-diagnostics`   | `pt-diagnostics`      | `pi-top diagnostics`        | `python3-pitop`            |
| `pt-battery`       | `pt-device-manager`   | `pi-top battery`            | `python3-pitop`            |
| `pt-brightness`    | `pt-device-manager`   | `pi-top display brightness` | `python3-pitop`            |
| `pt-devices`       | `pt-device-manager`   | `pi-top devices`            | `python3-pitop`            |
| `pt-host`          | `pt-device-manager`   | `pi-top devices hub`        | `python3-pitop`            |
| `pt-oled`          | `pt-device-manager`   | `pi-top oled write`         | `python3-pitop`            |

### Python Modules

| Legacy Python Module | Legacy Debian Package   | Superceding Python Module  | Superceding Debian Package |
|----------------------|-------------------------|----------------------------|----------------------------|
| `ptbuttons`          | `python3-pt-buttons`    | `pitop.miniscreen.buttons` | `python3-pitop`            |
| `ptoled`             | `python3-pt-oled`       | `pitop.miniscreen.oled`    | `python3-pitop`            |
| `ptpma`              | `python3-pt-pma`        | `pitop.pma`                | `python3-pitop`            |
| `ptprotoplus`        | `python3-pt-proto-plus` | `pitop.protoplus`          | `python3-pitop`            |
