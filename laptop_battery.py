import psutil
import tkinter.messagebox
battery = psutil.sensors_battery()

if battery.percent >= 95 and battery.power_plugged:
    tkinter.messagebox.showinfo(title="Un-Plug Battery",message=f"Battery now {battery.percent}! Please unplug the charger")
