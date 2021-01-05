from pitop.miniscreen.oled import (  # noqa: F401
    OLED as PTOLEDDisplay,
)
from pitop.miniscreen.oled.core import (  # noqa: F401
    fps_regulator,
)
from pitop.miniscreen.oled.core.controls import (  # noqa: F401
    get_device as get_device_instance,
    device_is_active as device_reserved,
    reset_device as reset_device_instance,
    set_control_to_pi as set_oled_control_to_pi,
    set_control_to_hub as set_oled_control_to_hub
)
import pitop.miniscreen.oled.core.controls as device_helper  # noqa: F401
canvas = PTOLEDDisplay().canvas

print("Note: Use of the 'ptoled' package is now deprecated. Please use 'pitop.miniscreen.oled' instead.")
print("For more information, please see https://github.com/pi-top/pi-top-Python-SDK-Migration-Support")
