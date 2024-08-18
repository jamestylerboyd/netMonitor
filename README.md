# Ethernet Connection Monitor

This Python script monitors your Ethernet connection in real-time, plays an alert sound when the connection is lost, and logs connection events. It's designed to run on Ubuntu within a Conda environment.

## Features

- Continuously monitors Ethernet connection
- Plays a siren sound at full volume when the connection is lost
- Stops the siren when the connection is restored or the script is terminated
- Logs all connection events (loss, restoration, and script termination) with timestamps
- Graceful termination handling

## Prerequisites

- Ubuntu operating system
- Anaconda or Miniconda installed
- An audio file named `siren_sound.mp3` in the same directory as the script

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/jamestylerboyd/netMonitor.git
   cd netMonitor
   ```

2. **Set up the Conda environment**

   Open a terminal and run the following commands:

   ```bash
   # Create a new Conda environment
   conda create -n netMonitor python=3.8

   # Activate the environment
   conda activate netMonitor

   # Install required packages
   conda install -c conda-forge pygame
   ```

3. **Prepare the audio file**

   Ensure that `siren_sound.mp3` is in the same directory as the script. If you don't have a siren sound, you can download a free one from various online sources.

## Usage

1. **Activate the Conda environment**

   ```bash
   conda activate netMonitor
   ```

2. **Run the script**

   ```bash
   python net_monitor.py
   ```

3. **Terminating the script**

   Press `Ctrl+C` to stop the script. The script will handle this gracefully, stopping the siren (if playing) and logging the termination event.

## Log File

The script creates a log file named `connection_log.txt` in the same directory. This file contains detailed information about each connection event:

- Connection loss start time
- Connection restoration time
- Duration of connection loss
- Script termination events

## Troubleshooting

1. **No sound**
   - Ensure your system volume is not muted
   - Check if `siren_sound.mp3` is in the correct directory
   - Verify that you have the necessary audio codecs installed

2. **Script crashes**
   - Check the console output for error messages
   - Ensure you're running the script with Python 3
   - Verify that all required packages are installed in your Conda environment

3. **False positives/negatives**
   - The script checks the connection by attempting to reach Google's DNS (8.8.8.8). If you're in a network that blocks this, you may need to modify the script to use a different reliable server.

## Customization

- To change the alert sound, replace `siren_sound.mp3` with your preferred audio file (keeping the same filename)
- To adjust the connection check frequency, modify the `time.sleep(1)` value in the main loop
- To log to a different file, change the filename in the `log_event` function

## License

MIT License 2024
