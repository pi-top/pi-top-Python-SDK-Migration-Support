from pitop.pma import (  # noqa: F401
    ForwardDirection,
    Direction,
    BrakingType,
    ServoMotor as PMAServoMotor,
    EncoderMotor as PMAEncoderMotor,
    UltrasonicSensor as PMAUltrasonicSensor,
    SoundSensor as PMASoundSensor,
    Potentiometer as PMAPotentiometer,
    LightSensor as PMALightSensor,
    LED as PMALed,
    Buzzer as PMABuzzer,
    Button as PMAButton
)
from pitop.camera import Camera as PMACamera  # noqa: F401
print("Note: Use of the 'ptpma' package is now deprecated. Please use 'pitop.pma' instead.")
print("For more information, please see https://github.com/pi-top/pi-top-Python-SDK-Migration-Support")
