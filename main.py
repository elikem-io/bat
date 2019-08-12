import wmi
from win10toast import ToastNotifier

toaster = ToastNotifier()
c = wmi.WMI()
for os in c.win32_Battery():
    remaining = os.EstimatedChargeRemaining

    if remaining >= 60:
       toaster.show_toast("Remove the charger! Faulty battery.",
        icon_path=None,
                   duration=10
       )
       print(os.ExpectedBatteryLife )
    elif remaining <= 40:
        print("Plug your charger! Faulty battery.")