//참고 문헌 
//https://infoinno.info/41 
//https://blog.naver.com/PostView.naver?blogId=boilmint7&logNo=220929664274
//https://blog.naver.com/PostView.naver?blogId=eduino&logNo=221066151223&categoryNo=21&parentCategoryNo=0


//All library
#include <DHT.h>
#include <DHT_U.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <MQUnifiedsensor.h>
#include "DHT.h"


//define pin 
#define DHTPIN 7    // modify to the pin we connected
#define DHTTYPE DHT22   // DHT 22  (AM2302)//temperature humidity 
DHT dht(8, DHT22);

//led,buzzer,flame
int redLed = 12;
int greenLed = 11;
int buzzer = 10;
int smokeA0 = A4;
int flameA0 = A5; 

// Your threshold value (Can change, test필요, 150~200 / 700~800 사이로 조정해서 오차 최적화)
int sensorThres = 800; //gas sensor
int sensorThres2 = 800; //flame sensor 


//segment setting
int leds[]={2,3,4,5,6,7,8,9}; //지정된 7segment 번호 
int led_num=8 ;//7segment led선언 
int num=0 ;//현재에 표시되고 있는 숫자 

//7segment 선언 

int set_number[10][8]={
  {0,0,0,0,0,0,1,1}, //0
  {1,0,0,1,1,1,1,1}, //1
  {0,0,1,0,0,1,0,1}, //2
  {0,0,0,0,1,1,0,1}, //3
  {1,0,0,1,1,0,0,1}, //4
  {0,1,0,0,1,0,0,1}, //5
  {0,1,0,0,0,0,0,1}, //6
  {0,0,0,1,1,1,1,1}, //7
  {0,0,0,0,0,0,0,1}, //8
  {0,0,0,0,1,0,0,1}, //9

};

//lcd패널 setting
LiquidCrystal_I2C lcd(0x27,20,4); //type 

void setup() {
  Serial.begin(9600);
  Serial.begin(9600); 


  dht.begin();

  //-----------------------
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(smokeA0, INPUT);
  pinMode(flameA0, INPUT);
  Serial.begin(9600);

  //lcd패널
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);

  lcd.print("Please evacuate!");

  lcd.setCursor(3,1);
  lcd.print("Do not evacuate the marked floor!");

}

void loop() {

  delay(1000);

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float hic = dht.computeHeatIndex(t,h,false);
  
 
  
  Serial.print("Humidity: "); 
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: "); 
  Serial.print(t);
  Serial.println(" *C");
  Serial.print(hic); 
  Serial.println(" *C ");




  int analogSensor = analogRead(smokeA0);
  int analogSensor2 = analogRead(flameA0);




  Serial.print("Gas Sensor Value : ");
  Serial.println(analogSensor);
  Serial.print("Flame Sensor Value : ");
  Serial.println(analogSensor2);
 

  if(analogSensor > sensorThres){
    digitalWrite(redLed, HIGH);
    digitalWrite(greenLed, LOW);
    tone(buzzer, 1000, 500);
    digitalWrite(leds[9],set_number[num][7]); //7 출력 
    if(analogSensor > 800){
      digitalWrite(leds[9],set_number[num][9]); //9 출력
      lcd.print("Do not move to the third floor"); //3층으로 이동 금지 
    }
  }

  else{
    digitalWrite(redLed,LOW);
    digitalWrite(greenLed,HIGH);
    noTone(buzzer);
    digitalWrite(leds[0],set_number[num][0]); //0출력 
  }

  if(analogSensor2 > sensorThres2){
    digitalWrite(redLed,HIGH);
    digitalWrite(greenLed,LOW);
    tone(buzzer,1000,500);
    digitalWrite(leds[9],set_number[num][7]); //7출력
    if(analogSensor > 800){
      digitalWrite(leds[9],set_number[num][9]);
      lcd.print("Do not move to the elevator");
    }
  } 

  else
  {
    digitalWrite(redLed,LOW);
    digitalWrite(greenLed,HIGH);
    digitalWrite(leds[0],set_number[num][0]); //0출력 
  }
  
  
  
  delay(1000);

}


