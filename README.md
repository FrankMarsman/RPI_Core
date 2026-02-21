# pi_status_monitor.py

## Overview
The `pi_status_monitor.py` script is designed to monitor the status of a Raspberry Pi device. It periodically checks the system's health and provides detailed information for diagnostics.

## Features
- Monitor CPU temperature and usage
- Check memory usage
- Monitor disk space availability
- Send notifications if thresholds are exceeded

## Requirements
- Python 3.x
- Relevant libraries (e.g., psutil)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/FrankMarsman/RPI_Core.git
   cd RPI_Core
   ```
2. Install the required packages:
   ```bash
   pip install psutil
   ```

## Usage
Run the script from the command line:
```bash
python pi_status_monitor.py
```

## Configuration
Modify settings such as thresholds and notification methods directly in the script as needed.

## Author
Frank Marsman

## License
This project is licensed under the MIT License.