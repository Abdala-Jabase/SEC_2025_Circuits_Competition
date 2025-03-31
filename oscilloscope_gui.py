import serial
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time
import math
from collections import deque
start_time=time.time()
arduino = serial.Serial(port='COM3',  baudrate=115200, timeout=1)


plt.ion()
fig, ax = plt.subplots()
ax.set_ylim(-5.5,5.5)
x_data = deque([], maxlen=100)
y_data = deque([], maxlen=100)
line, = ax.plot(x_data, y_data)
offset_voltage=3.5
# Axis labels
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title("Waveform Data")
    
new_data=0
max_x=0
min_x=0

min_text = ax.text(0, 0, "", color="blue", fontsize=10)
max_text = ax.text(0, 0, "", color="green", fontsize=10)
peak_text = ax.text(0, 0, "", color="red", fontsize=10)
avg_text= ax.text(0, 0, "", color="purple", fontsize=10)

max_text.set_position((time.time()-start_time+0.01, 5.2))
min_text.set_position((time.time()-start_time+0.02, 5))
max_text.set_text(f"Max: {max_x}")
min_text.set_text(f"Min: {min_x}")

while True:
    old_data=new_data
    try:
        x_data.append(time.time()-start_time)
        y_data.append(new_data)
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        ax.relim()
        ax.set_ylim(-5.5,5.6)
        ax.autoscale_view()
        max_text.set_position((x_data[0]+4.5, 5.25))
        min_text.set_position((x_data[0]+4.5, 4.9))
        peak_text.set_position((x_data[0]+4.5, 4.65))
        avg_text.set_position((x_data[0]+4.5, 4.30))
        max_text.set_text(f"Max: {max(y_data):.2f}")
        min_text.set_text(f"Min: {min(y_data):.2f}")
        peak_text.set_text(f"P2P: {max(y_data)-min(y_data):.2f}")
        avg_text.set_text(f"Avg: {sum(y_data)/len(y_data):.2f}")
        fig.canvas.draw()
        fig.canvas.flush_events()
        new_data = int(arduino.readline().decode().strip())*0.0244-offset_voltage
        if new_data > max_x:
            max_x=new_data
        if new_data < min_x:
            min_x=new_data
        arduino.reset_input_buffer()
        time.sleep(0.02)

    except:
        x_data.append(time.time()-start_time)
        y_data.append(old_data)
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        ax.relim()
        ax.set_ylim(-5.5,5.6)
        ax.autoscale_view()
        peak_text.set_position((x_data[0]+4.5, 4.65))
        avg_text.set_position((x_data[0]+4.5, 4.30))
        max_text.set_position((x_data[0]+4.5, 5.25))
        min_text.set_position((x_data[0]+4.5, 4.9))
        max_text.set_text(f"Max: {max(y_data):.2f}")
        min_text.set_text(f"Min: {min(y_data):.2f}")
        peak_text.set_text(f"P2P: {max(y_data)-min(y_data):.2f}")
        avg_text.set_text(f"Avg: {sum(y_data)/len(y_data):.2f}")
        fig.canvas.draw()
        fig.canvas.flush_events()
        old_data=new_data
        arduino.reset_input_buffer()
        time.sleep(0.02)

new_data=int(0)

# print(time.time())
update_plot(new_data)