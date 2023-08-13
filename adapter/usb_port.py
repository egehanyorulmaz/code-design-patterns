class UsbCable:
    def __init__(self):
        self.isPlugged = False

    def plugUsb(self):
        self.isPlugged = True


class UsbPort:
    def __init__(self):
        self.portAvailable = True

    def plug(self, usb):
        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False


# UsbCables can plug directly into Usb ports
usbCable = UsbCable()
usbPort1 = UsbPort()
usbPort1.plug(usbCable)


class MicroUsbCable:
    def __init__(self):
        self.isPlugged = False

    def plugMicroUsb(self):
        self.isPlugged = True


class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable):
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()

    # can override UsbCable.plugUsb() if needed


# MicroUsbCables can plug into Usb ports via an adapter
microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())
usbPort2 = UsbPort()
usbPort2.plug(microToUsbAdapter)
