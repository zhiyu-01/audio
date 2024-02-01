import pyaudio

audio = pyaudio.PyAudio()

# get device count
device_count = audio.get_device_count()
print(f"device count: {device_count}")

# get device info
for i in range(device_count):
    device_info = audio.get_device_info_by_index(i)
    print(f"device {i}: {device_info}")

print("default input device: ", audio.get_default_input_device_info())
print("default output device: ", audio.get_default_output_device_info())