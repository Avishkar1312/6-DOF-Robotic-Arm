#include <AccelStepper.h>

#define STEP_PIN_M1 2    //Step pin of Base_Motor
#define DIR_PIN_M1 5     //Direction pin of Base_Motor
#define STEP_PIN_M2 3    //Step pin of Shoulder_Motor
#define DIR_PIN_M2 6     //Direction pin ofShoulder_Motor  
#define En_Pin1 8  //Assigning a name to the unified enable pin of all the stepper drivers on the cnc shield


AccelStepper stepperM1(AccelStepper::DRIVER, STEP_PIN_M1, DIR_PIN_M1);      //Defining Base_motor
AccelStepper stepperM2(AccelStepper::DRIVER, STEP_PIN_M2, DIR_PIN_M2);      //Defining Shoulder_motor

String input = "";

void setup() {
  Serial.begin(9600);
  pinMode(En_Pin1,OUTPUT);
  digitalWrite(En_Pin1,LOW);   // Making the unified enable pin low so that all stepper drivers are functional
  stepperM1.setAcceleration(500);    /// these values are set to smoothen the position and to avoid any jittery consequences
  stepperM1.setMaxSpeed(400); // default
  stepperM2.setAcceleration(500);
  stepperM2.setMaxSpeed(400); // default
}

void loop() {                           // Used to read the incoming serial outputs from the raspi5
  if (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      parseCommand(input);
      input = "";
    } else {
      input += c;
    }
  }


  stepperM1.run();                     //Keeps the current running in the base_motor so that it holds its position
  stepperM2.run();                     //Keeps the current running in the shoulder_motor so that it holds its position
}

void parseCommand(String cmd) {                                //Used to parse the incoming angle and speed commands from teh raspi5
  cmd.trim();

  int firstSpace = cmd.indexOf(' ');
  int secondSpace = cmd.indexOf(' ', firstSpace + 1);
  int thirdSpace = cmd.indexOf(' ', secondSpace + 1);


  float angle1 = cmd.substring(0, firstSpace).toFloat();
  float speed1 = cmd.substring(firstSpace + 1, secondSpace).toFloat();
  float angle2 = cmd.substring(secondSpace + 1, thirdSpace).toFloat();
  float speed2 = cmd.substring(thirdSpace + 1).toFloat();
  base_Motor(angle1,speed1);
  shoulder_Motor(angle2,speed2);


  }


void base_Motor(float angle1,float speed1) {
  stepperM1.moveTo(angleToSteps(angle1*10*180/3.14));            // 180/3.14 is used to convert the angle from radians to degrees
  Serial.print("base motor moving: ");                           //angle1 is multiplied by 10 as the gear ratio of the bottom gear is 10
  Serial.println(angle1*180/3.14);                               //Actual angle1 in degrees is printed

  
  while (stepperM1.isRunning()) {
    stepperM1.run();
  }

  Serial.println("base_motor ran");  
}

void shoulder_Motor(float angle2, float speed2){

  stepperM2.moveTo(angleToSteps(angle2*3.7*180/3.14));            // 180/3.14 is used to convert the angle from radians to degrees
  Serial.println("shoulder motor moving: ");                      //angle2 is multiplied by 3.7 as the gear ratio of the shoulder gearbox is 3.7
  Serial.println(angle2*180/3.14);                                //Actual angle2 in degrees is printed

  while(stepperM2.isRunning()){
    stepperM2.run();
  }
  Serial.println("shoulder motor ran");
  Serial.println("done");

}

int angleToSteps(float angle) {                                   //Steps for the motor are decided for the corresponding angle
  return angle / 1.8;                                             //Full Step mode
}
