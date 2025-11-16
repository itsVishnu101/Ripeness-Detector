## 1. Project Overview

This repository contains code, documentation, and configuration for an **IoT Ripeness Detector** — an embedded system that inspects fruit/vegetable samples and predicts ripeness using sensor readings and a lightweight ML model. The device can be built using a **Raspberry Pi Zero W** (camera-based) or an **ESP32-CAM** module (sensor + camera) depending on cost and compute needs.

I built this during my B.Tech final year/minor project to learn embedded systems, computer vision, and edge ML. The goal was to provide farmers and small vendors an accessible device to make harvesting and selling decisions more data-driven.

---

## 2. What I Built (Features)

* Real-time ripeness classification (Unripe / Ripe / Overripe)
* Two hardware flavours supported:

  * **Raspberry Pi Zero W** with a camera for CNN inference using TFLite
  * **ESP32-CAM** for lightweight capture + sensor-based heuristic or offloading inference
* Local web UI (Pi Zero) / Basic API (ESP32)
* MQTT & HTTP endpoints for publishing results
* Calibration routine and CSV logging

---

## 3. Hardware & Components (Specific)

### **Primary Tested Setup**

* **Raspberry Pi Zero W** (Camera-capable, Wi-Fi)
* **ESP32-CAM (AI-Thinker)** — secondary capture/edge node
* **TCS34725 Color Sensor** (optional)
* **LED Ring / White LED Lighting** for consistent illumination
* **Power:**

  * Pi Zero W → 5V USB supply (2A recommended)
  * ESP32-CAM → 5V (with regulator if needed)
* **Others:** jumper wires, breadboard, microSD card

**Notes:**

* Pi Zero W has limited CPU → use **quantized TFLite models**.
* ESP32-CAM is limited → best for image offload or simple heuristics.

---

## 4. Software Stack

* **Pi Zero W:** Python 3, OpenCV, TensorFlow Lite, Flask (UI), paho-mqtt
* **ESP32-CAM:** Arduino/PlatformIO firmware for:

  * Camera streaming
  * Sample capture
  * MQTT/HTTP posting
* **Scripts:** `capture_sample.py`, `preprocess.py`, `train.py`, `app.py`

---

## 5. System Architecture

```
[ESP32-CAM ]      [Raspberry Pi Zero W]
     |                           |
 image capture -> MQTT/HTTP -> local inference (TFLite) -> UI / Logger
                                    |
                             publish to broker
```

Use ESP32-CAM as a low-cost remote capture module.

---

## 6. Wiring & Connections (Pi Zero W + ESP32-CAM)

### **Raspberry Pi Zero W (CSI or USB Camera)**

* Attach CSI ribbon cable correctly.
* Enable camera:

```
sudo raspi-config
Interface Options → Camera → Enable
```

* Power with stable 5V 2A.
* LED Ring → GPIO (control pin) + 5V + GND (use MOSFET for high-current LEDs).

### **ESP32-CAM (AI-Thinker Module)**

* **Power:** 5V → VIN (module expects 5V; ensure enough current).
* Camera ribbon is built-in.
* **Flash LED:** connect LED to GPIO4 via resistor.

### **TCS34725 Sensor with ESP32-CAM**

* SDA → GPIO21
* SCL → GPIO22
* VIN → 3.3V (or 5V depending on module)
* GND → GND

**Important ESP32-CAM Notes:**

* Limited GPIO → check board pinout.
* Use stable power to avoid **brownouts** during Wi-Fi + camera use.

---

## 7. Setup — Step by Step

### **A. Raspberry Pi Zero W Setup**

1. Flash Raspberry Pi OS Lite and boot.
2. Enable camera, SSH, I2C:

```
sudo raspi-config
```

3. Install dependencies:

```
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-opencv libatlas-base-dev -y
pip3 install -r requirements.txt
```

4. Configure:

```
cp config.example.yaml config.yaml
```

5. Run server:

```
python3 app.py
```

Open in browser: `http://<pi-ip>:5000`

### **B. ESP32-CAM Setup**

1. Open `esp32/esp32-cam.ino` in Arduino IDE/PlatformIO.
2. Add Wi-Fi + MQTT/server credentials.
3. Select board: **AI-Thinker ESP32-CAM**.
4. Flash using FTDI:

   * Connect **U0R/U0T** + **IO0 → GND** during flashing.
5. After reboot:

   * Video stream: `http://<esp32-ip>/stream`
   * Image upload: POST to: `http://<pi-ip>:5000/upload`

---

## 8. How the Model Works

### **Pi Zero W Workflow**

1. Capture image
2. Resize to 224×224, normalize
3. Run TFLite model (quantized int8)
4. Output: ripeness class probabilities

### **ESP32-CAM Workflow**

* Capture → send image to Pi/server for inference
* OR compute simple RGB statistics and send features

**Performance:**

* Pi Zero W (quantized model): **300–800 ms** per inference
* ESP32-CAM: sub-second heuristics; network-dependent streaming

---

## 9. Data Format

```
/data/images/fruit_YYYYMMDD_HHMMSS.jpg
labels.csv → filename,label,fruit_type,date_taken,notes
sensors.csv → timestamp,fruit_type,r,g,b,clear,temp,humidity,label
```

Run:

```
python3 preprocess.py
```

---

## 10. Running the Project

Start server:

```
python3 app.py
```

Capture from Pi:

```
python3 capture_sample.py --fruit banana --save
```

ESP32-CAM → POST image to `/upload`.

### **Sample config.yaml**

```yaml
device: pi_zero_w
camera_index: 0
model_path: model/ripeness_quantized.tflite
mqtt:
  broker: 192.168.1.100
  port: 1883
  topic: farm/ripeness
```

---

## 11. Calibration & Testing

* Use white reference card for color calibration.
* Keep lighting consistent.
* Minimum **200 images per fruit type** for good model training.

---

## 12. Troubleshooting

* **ESP32-CAM brownouts:** use dedicated 5V supply + capacitor.
* **Pi Zero camera failure:** recheck ribbon, enable camera.
* **Slow inference:** use smaller/quantized model.

---

## 13. Future Improvements

* Upgrade to **Pi Zero 2 W** for better inference speed.
* Train fruit-specific models.
* Use **TinyML**

##  Connect with me:

<p align="left" style="display: flex; gap: 10px;">

  <a href="https://www.linkedin.com/in/its-vishnu-verma/" target="_blank" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>

  <a href="mailto:ui22ec86@iiitsurat.ac.in" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white">
  </a>

</p>

