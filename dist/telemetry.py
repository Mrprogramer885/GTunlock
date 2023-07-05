import psutil
import platform
import cpuinfo
import GPUtil
import webbrowser
import time
from datetime import datetime

def telemdata():
    cpu_percent = psutil.cpu_percent()
memory_info = psutil.virtual_memory()
system_info = platform.uname()
cpu_info = cpuinfo.get_cpu_info()
gpus = GPUtil.getGPUs()

# Get browser information
browser_name = webbrowser.get().name

# Create a timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create the telemetry string
telemetry = f"Timestamp: {timestamp}\nMemory Info: {memory_info}\n"
telemetry += f"System Info: {system_info}\n"
telemetry += f"GPU Type and Info:\n"

for i, gpu in enumerate(gpus):
    telemetry += f"GPU {i + 1}: {gpu.name}, Memory Utilization: {gpu.memoryUtil}%\n"

telemetry += f"Browser Name: {browser_name}\n"

# Define the output file path
output_file = "system_telemetry.txt"

# Write telemetry to the file
with open(output_file, "a") as file:
    file.write(telemetry + "\n\n")

print("telemetry data created. thay can be found at: system_telemetry.txt")