from PyQt5.QtMultimedia import QCameraInfo

def list_available_cameras():
    cameras = QCameraInfo.availableCameras()
    for camera in cameras:
        print(f"Camera Name: {camera.description()}, Index: {camera.deviceName()}")

# 列出可用摄像头设备的信息及索引
list_available_cameras()
