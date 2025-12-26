## 📌 Project Overview

This repository contains code, documentation, and configuration for an **IoT Ripeness Detector** — an embedded system that inspects fruit/vegetable samples and predicts ripeness using sensor readings and a lightweight ML model. The device can be built using a **ESP8266 microcontroller**  depending on cost and compute needs.

I built this during my B.Tech final year/minor project to learn embedded systems, computer vision, and edge ML. The goal was to provide farmers and small vendors an accessible device to make harvesting and selling decisions more data-driven.

---
## 📄 Project Report

The complete project report containing system overview, architecture, implementation details and results is  here:

🔗 **[IoT-Based Ripeness Detection for Vertical Farming – Project Report (PDF)](https://drive.google.com/file/d/1z2VIhk07d0sxIXvT7gKLdUFoxTHR1r8Z/view?usp=drive_link)**



## ✨ What I Built (Features)

* Real-time ripeness classification (Unripe / Ripe / Overripe)
* Two hardware flavours supported:

  * ESP8266-based Wi-Fi communication and physical LED indication
  * Web interface for image upload, result display, and scan history 
* FastAPI backend for real-time image analysis


---

## 🧰 Hardware & Components (Specific)

### **Primary Tested Setup**

* ESP8266 Wi-Fi Microcontroller
* Red and Green LEDs for ripeness indication
* Breadboard and jumper wires 
* Smartphone for image capture and upload
* Laptop / PC running the FastAPI backend server
---

## 💻 Software Stack

* Backend: Python, FastAPI, OpenCV, NumPy
* Frontend: HTML, CSS, JavaScript
* Firmware: Arduino C++ (ESP8266)
* Communication: HTTP and JSON over Wi-Fi

---

## 🏗️ System Architecture

```
[ Smartphone / Browser ]
           |
           | Image Upload (HTTP)
           v
[ FastAPI Backend (Python + OpenCV) ]
           |
           | JSON Response (Wi-Fi)
           v
[ ESP8266 Microcontroller ]
           |
           | GPIO Control
           v
[ LED Indicators ]
```

The architecture demonstrates a complete IoT pipeline involving sensing, computation, communication, and actuation.
---

## ⚙️ Wiring & Connections (Pi Zero W + ESP32-CAM)

* ESP8266 Connections
* VCC → 3.3V
* GND → Ground
* Red LED → GPIO pin (with resistor)
* Green LED → GPIO pin (with resistor)


## 🔮 Future Improvements

* Integration of machine-learning models for higher accuracy
* Multi-sensor fusion (temperature, moisture, humidity)
* Cloud-based monitoring and analytics
* Mobile application support
* Automatic multi-fruit detection

## 📫 Connect with me:

<p align="left">
  <a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>
    <a href="https://www.linkedin.com/in/its-vishnu-verma/" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
