#include <Servo.h>


// 舵机控制引脚
const int servoPin = D5;
Servo servo;

// 串口通信参数
const int baudRate = 115200;

// 定义舵机初始角度和目标角度
const int initialAngle = 90;
const int targetAngle = 180;

// 定义舵机转动速度
const int servoSpeed = 1; // 舵机转动速度，可以根据需要调整

bool servoMoving = false;

void setup() {
  // 初始化舵机引脚
  servo.attach(servoPin);

  // 初始化串口通信
  Serial.begin(baudRate);
  
  // 将舵机移动到初始位置
  servo.write(initialAngle);
}

void loop() {
  // 检查串口是否有数据可用
    Serial.printf("waiting......\n");
    // 读取串口输入
    int command = Serial.parseInt();
    servo.write(90);
    // 如果收到字符'1'，并且舵机当前不在运动中，则开始转动舵机
    if (command == 1 && !servoMoving) {
      //servoMoving = true;
      //moveServo();
       servo.write(targetAngle);
       delay(5000);
       servo.write(90);//停止了
    }
  
  
  // 检查舵机是否在运动中，如果是，则更新舵机角度
  if (servoMoving) {
    if (servo.read() == targetAngle) {
      // 舵机已经到达目标位置，复位并停止运动
      servoMoving = false;
      servo.write(initialAngle);
    }
  }
}


