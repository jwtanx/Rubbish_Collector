# IMPORTANT: MAKE SURE THIS SCRIPT IS RAN FIRST BEFORE THE INFERENCE
# OR run this when there is new update for the model rubbish_detector.pt
import os
import gdown
import platform

# Updating the current script in the yolov5 folder
if platform.system() == "Windows":
    os.system("copy rubbish_collector.py yolov5")
else:
    os.system("cp ./rubbish_collector.py ./yolov5")

# Downloading the latest version
gdown.download(id="1_8bgnMVvRI8wwsBtV9SksVJ2nim5rVoW", output="./rubbish_detector.pt")

print("STATUS: COMPLETED")
print("Copy and paste the command below to run the inferencing\npython ./yolov5/rubbish_collector.py --weights ./rubbish_detector.pt --source 2 --nosave")