# IEEE SoutheastCon 2025 Circuit Competition

## Digital Oscilloscope Design & Guide

### Group 6B
**Date:** 03/28/2025

---

## Overview
This project presents a digital oscilloscope designed for the IEEE SoutheastCon 2025 Circuit Competition. The goal was to create a functional oscilloscope that can plot voltages cleanly while incorporating improvements to enhance its usability.

---

## Design Rationale
The initial step was to build a basic oscilloscope capable of displaying voltage waveforms accurately. Enhancements were made to increase the range of measurable voltages and implement the ability to read negative voltages.

---

## Challenges and Solutions

### Baud Rate
- The original setup used a baud rate of **9600**, which was later increased to **115200** to improve the responsiveness of the waveform program and minimize clipping.

### Recursion Issue
- The original oscilloscope code used recursion, which caused a **stack overflow** after 40-45 seconds.
- The solution was to replace the recursive function with a **while loop**, preventing crashes and ensuring continuous operation.

### Negative Voltage Reading
- The **Arduino Mega 2560** cannot directly read negative voltages as it could damage the microcontroller.
- Attempts to use diodes failed due to their inherent voltage drop affecting the accuracy of readings.
- A **voltage shifting technique** was implemented using a **9V battery reference** and a **voltage divider** with **two 10kΩ resistors**, allowing voltage readings from **-4.5V to 4.5V**.

---

## Operation Guide
1. Install **Arduino IDE** and **Python**.
2. Upload the Arduino sketch to the **Arduino Mega 2560**.
3. Run the Python script to start the oscilloscope display.
4. The waveform should appear, displaying real-time voltage data.


---

## Innovative Aspects
### Voltage Shifting and Expansion
- Since the **Arduino ADC** is limited to **0-5V**, a sensor with a built-in **voltage divider** was used to scale **0-25V** down to **0-5V**.
- A voltage reference shift allowed the oscilloscope to interpret negative voltages, setting **4.5V as the new ground level**.
- High resistance values (10kΩ resistors) were used to improve power efficiency.

### Python Interface
- A Python-based interface was implemented for **enhanced user experience and customization**.
- Added real-time calculations for:
  - **Peak-to-Peak Voltage**
  - **Average Voltage**
  - **Maximum & Minimum Voltage**
- Used the **matplotlib** library for graphical representation.

---

## Conclusion
Our digital oscilloscope is a **more customizable and responsive alternative** to the default **Arduino Serial Monitor**. By leveraging **Python's simplicity and extensive documentation**, we successfully built a flexible, user-friendly tool for waveform visualization.

---

## Future Improvements
- Add **FFT analysis** for frequency domain visualization.
- Improve GUI with **Tkinter or PyQt**.
- Implement **data logging features** for waveform storage and review.

---

## Contributors
- Abdala Jabase
- Adam Moore
- Brian Luckett

---

## Demonstration Video
Watch the project in action: [YouTube Link](https://youtube.com/shorts/GEBlHFlLf4g?feature=share)



