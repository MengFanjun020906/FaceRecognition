#include <Servo.h>

#include <ArduinoMqttClient.h>
#include <ESP8266WiFi.h>

// 舵机控制引脚
const int servoPin = D5;
Servo servo;

// 串口通信参数
const int baudRate = 9600;

// 定义舵机初始角度和目标角度
const int initialAngle = 90;
const int targetAngle = 180;

// 定义舵机转动速度
const int servoSpeed = 1; // 舵机转动速度，可以根据需要调整

bool servoMoving = false;

char ssid[] = "meng";    // your network SSID (name)
char pass[] = "25197758";    // your network password (use for WPA, or use as key for WEP)


WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const char broker[]    = "iot-06z00eaojla1tr3.mqtt.iothub.aliyuncs.com";
int        port        = 1883;

const char inTopic[]   = "/sys/k15pz2oiJaP/Cloud/thing/service/property/set";
const char outTopic[]  = "/sys/k15pz2oiJaP/MG996R/thing/service/property/set";

const long interval = 10000;
unsigned long previousMillis = 0;

int count = 0;

void setup() {

   // 初始化舵机引脚
  servo.attach(servoPin);

  // 初始化串口通信
  Serial.begin(baudRate);
  
  // 将舵机移动到初始位置
  servo.write(initialAngle);
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // attempt to connect to WiFi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

mqttClient.setId("k15pz2oiJaP.MG996R|securemode=2,signmethod=hmacsha256,timestamp=1713862406063|");
mqttClient.setUsernamePassword("MG996R&k15pz2oiJaP","39ab0c4c3dc156df441d38bf1578371726899ca7db789739beb141fce70aa6cf");

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  Serial.println();

  // set the message receive callback
  mqttClient.onMessage(onMqttMessage);

  Serial.print("Subscribing to topic: ");
  Serial.println(inTopic);
  Serial.println();

  int subscribeQos = 1;

  mqttClient.subscribe(inTopic, subscribeQos);


  Serial.print("Waiting for messages on topic: ");
  Serial.println(inTopic);
  Serial.println();
}

void loop() {

    int command = Serial.parseInt();
    servo.write(90);
    mqttClient.poll();
    String payload;

      if (command == 1 && !servoMoving) {
      //servoMoving = true;
      //moveServo();
       servo.write(targetAngle);
       delay(5000);
       servo.write(90);//停止了
      unsigned long currentMillis = millis();
       if (currentMillis - previousMillis >= interval) {

    previousMillis = currentMillis;
    payload += "Start!";
    //payload += "hello world!";
    //payload += " ";
    //payload += count;

    Serial.print("Sending message to topic: ");
    Serial.println(outTopic);
    Serial.println(payload);



    bool retained = false;
    int qos = 1;
    bool dup = false;

    mqttClient.beginMessage(outTopic, payload.length(), retained, qos, dup);
    mqttClient.print(payload);
    mqttClient.endMessage();

    Serial.println();

    count++;
  }

       
  }
  
  
  // 检查舵机是否在运动中，如果是，则更新舵机角度
  if (servoMoving) {
    if (servo.read() == targetAngle) {
      // 舵机已经到达目标位置，复位并停止运动
      servoMoving = false;
      servo.write(initialAngle);
    }
  }

  //unsigned long currentMillis = millis();

  // 读取串口输入


  // if (currentMillis - previousMillis >= interval) {

  //   previousMillis = currentMillis;
  //   payload += "hello world!";
  //   //payload += " ";
  //   //payload += count;

  //   Serial.print("Sending message to topic: ");
  //   Serial.println(outTopic);
  //   Serial.println(payload);



  //   bool retained = false;
  //   int qos = 1;
  //   bool dup = false;

  //   mqttClient.beginMessage(outTopic, payload.length(), retained, qos, dup);
  //   mqttClient.print(payload);
  //   mqttClient.endMessage();

  //   Serial.println();

  //   count++;
  // }
}

void onMqttMessage(int messageSize) {
  // we received a message, print out the topic and contents
  Serial.print("Received a message with topic '");
  Serial.print(mqttClient.messageTopic());
  Serial.print("', duplicate = ");
  Serial.print(mqttClient.messageDup() ? "true" : "false");
  Serial.print(", QoS = ");
  Serial.print(mqttClient.messageQoS());
  Serial.print(", retained = ");
  Serial.print(mqttClient.messageRetain() ? "true" : "false");
  Serial.print("', length ");
  Serial.print(messageSize);
  Serial.println(" bytes:");

  // use the Stream interface to print the contents
  while (mqttClient.available()) {
    Serial.print((char)mqttClient.read());
  }
  Serial.println();

  Serial.println();
}