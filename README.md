# Jupiter Robot: Rubbish Cleaner

## Ubuntu Setup
1. Open up a terminal and change your directory to a directory that you want the projec to be in.
2. Clone the project's GitHub here  
   ```git clone https://github.com/jwtanx/Rubbish_Collector .```
3. Clone the repo for yolov5  
   ```git clone https://github.com/ultralytics/yolov5```
4. Make sure you have python version 3.8 or above
   If not you can install the python3.8 but take note  
   **!!! DO NOT CHANGE THE PYTHON DEFAULT VERSION !!!**  
   ```sudo apt-get update```  
   ```sudo apt-get install python3.8 python3.8-dev python3.8-distutils python3.8-venv```
5. Create a virtual python virtual environement with >= Python 3.8  
   ```python3.8 -m venv jupiter```
6. Activate the virtual environment, when the environment is activated, you can see the (jupiter) on the left hand side of your command line  
   ```source jupiter/bin/activate```
7. Install the requirements, update your pip to the latest version if the installation stopped halfway  
   ```pip install -r requirements.txt```
8. **!!! IMPORTANT : FIRST TIME SETUP ONLY !!!**  
   ```python ./setup.py```  
   If your donwload for the model failed, head to this Google Drive [link](https://drive.google.com/uc?id=1_8bgnMVvRI8wwsBtV9SksVJ2nim5rVoW&export=download) and put the downloaded model pt file into this project directory.

## INFERENCING
1.  Start the inferencing on the robot camera  
   ```python ./yolov5/rubbish_collector.py --weights ./rubbish_detector.pt --source 2 --nosave```  
   Try replacing the `2` with `0` or `1` if the webcam is not working with `2`  
   When first time run, you might see ```requirements: torch!=1.12.0,>=1.7.0 not found and is required by YOLOv5, attempting auto-update...```
2. To quit, make sure the Python Window is focused and hold the `q` key until the window is exited
3. It is recommended to deactivate the environment when you want are done with the application  
   Type ```deactivate``` to deactivate the envuronment before you quit the terminal

## More information about Jupiter Robot here
1. [Jupiter Robot](https://www.lattelrobotics.com/jupiter-robot/) we are working with
2. [Documentation](https://wiki.ros.org/ROS/Tutorials) for the robot ROS