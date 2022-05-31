from easyhid import Enumeration as EasyHidEnum
from time import sleep


class HIDKeyboardError(Exception):
    pass


class SteelseriesKeyboardOled(object):
    def __init__(self):
        self.pids = {
            "ApexProTKL": 0x1614,
            "Apex7": 0x1612,
            "Apex7TKL": 0x1618,
            "ApexPro": 0x1610,
        }

    def find_keyboard(self, keyboard_pid):
        """ Enumerates Keyboard HID"""
        try:
            hid_enum = EasyHidEnum()
            keyboard = hid_enum.find(vid=0x1038, pid=keyboard_pid, interface=1)[0]
            return keyboard
        except IndexError:
            raise HIDKeyboardError("No Keyboard Detected")


def main():
    try:
        sko = SteelseriesKeyboardOled()
        keyboard = sko.find_keyboard(sko.pids.get("ApexProTKL"))
        keyboard.open()
        print(keyboard)
        keyboard.send_feature_report(bytearray([0x61] + [0x00] * 640 + [0x00]))
        print(keyboard.get_product_string())
        keyboard.close()
    except HIDKeyboardError as error_message:
        print(error_message)


if __name__ == "__main__":
    main()
