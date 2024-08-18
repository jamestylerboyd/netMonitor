import time
import socket
import pygame
from datetime import datetime
import signal
import sys

def check_ethernet():
    try:
        # Try to connect to a reliable server (Google's DNS)
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def log_event(event_type, start_time, end_time=None):
    with open("connection_log.txt", "a") as log_file:
        log_file.write(f"Event Type: {event_type}\n")
        log_file.write(f"Start Time: {start_time}\n")
        if end_time:
            downtime = end_time - start_time
            log_file.write(f"End Time: {end_time}\n")
            log_file.write(f"Total Duration: {downtime}\n")
        log_file.write("-" * 40 + "\n")

def signal_handler(sig, frame):
    global connection_lost, start_time
    print("\nScript terminated by user.")
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    if connection_lost:
        end_time = datetime.now()
        log_event("Connection Loss (Script Terminated)", start_time, end_time)
    else:
        log_event("Script Terminated (No ongoing connection loss)", datetime.now())
    sys.exit(0)

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("siren_sound.mp3")
pygame.mixer.music.set_volume(1.0)  # Set volume to maximum

print("Ethernet connection monitor started.")
print("Press Ctrl+C to stop the script.")

connection_lost = False
start_time = None

# Set up signal handler for graceful termination
signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        if check_ethernet():
            if connection_lost:
                print("Ethernet connection restored.")
                pygame.mixer.music.stop()
                end_time = datetime.now()
                log_event("Connection Restored", start_time, end_time)
                connection_lost = False
        else:
            if not connection_lost:
                print("Ethernet connection lost!")
                pygame.mixer.music.play(-1)  # Play on loop
                start_time = datetime.now()
                log_event("Connection Lost", start_time)
                connection_lost = True
        
        time.sleep(1)  # Check every second

except Exception as e:
    print(f"An error occurred: {e}")
    if connection_lost:
        end_time = datetime.now()
        log_event("Connection Loss (Script Error)", start_time, end_time)
    pygame.mixer.music.stop()
    pygame.mixer.quit()