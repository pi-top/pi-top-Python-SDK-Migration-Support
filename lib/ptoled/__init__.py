from pitop.miniscreen.oled import (  # noqa: F401
    OLED as PTOLEDDisplay,
)
from pitop.miniscreen.oled.core import (  # noqa: F401
    fps_regulator,
)


__o = PTOLEDDisplay()
canvas = __o.canvas


# Deprecated functions
def get_device_instance():
    return __o.get_device()


def device_reserved():
    return __o.device_is_active()


def reset_device_instance():
    __o.reset_device()


def set_oled_control_to_pi():
    __o.set_control_to_pi()


def set_oled_control_to_hub():
    __o.set_control_to_hub()


print("Note: Use of the 'ptoled' package is now deprecated. Please use 'pitop.miniscreen.oled' instead.")
print("For more information, please see https://github.com/pi-top/pi-top-Python-SDK-Migration-Support")
