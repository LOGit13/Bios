/* Stream raw 12-bit acceleration counts from the SparkFun BMA400.
   Install the SparkFun BMA400 Arduino Library through the Arduino Library Manager.

   The BMA400 uses I2C address 0x14 by default. On an Arduino Uno, connect
   SDA to A4 and SCL to A5. Use the breakout's supported supply voltage.
*/

#include <Wire.h>
#include "SparkFun_BMA400_Arduino_Library.h"
#include "SparkFun_Qwiic_OpenLog_Arduino_Library.h"
#define BMA400_ACCEL_DATA_REG 0x04


OpenLog myLog; //Create instance
const byte OpenLogAddress = 42; //Default Qwiic OpenLog I2C address
char filename[] = "ACCdata.txt";

BMA400 accel;

int16_t readRawAxis(uint8_t lsb, uint8_t msb) {
  int16_t value = ((uint16_t)msb << 8) | lsb;
  if (value > 2047) {
    value -= 4096;
  }
  return value;
}

void setup() {
  Serial.begin(57600);
  Wire.begin();
  myLog.begin(); //Open connection to OpenLog (no pun intended)
  delay(500);
  myLog.append(filename);

  if (accel.beginI2C() != BMA400_OK) {
    Serial.println("Not Connected. Please check connections and read the hookup guide.");
    while (1);
  }

  accel.setRange(BMA400_RANGE_8G);
  accel.setODR(BMA400_ODR_200HZ);
}

void loop() {
  Wire.beginTransmission(BMA400_I2C_ADDRESS_DEFAULT);
  Wire.write(BMA400_ACCEL_DATA_REG);
  if (Wire.endTransmission(false) != 0) {
    return;
  }

  if (Wire.requestFrom((uint8_t)BMA400_I2C_ADDRESS_DEFAULT, (uint8_t)6) == 6) {
    uint8_t xLsb = Wire.read();
    uint8_t xMsb = Wire.read();
    uint8_t yLsb = Wire.read();
    uint8_t yMsb = Wire.read();
    uint8_t zLsb = Wire.read();
    uint8_t zMsb = Wire.read();

    myLog.print(readRawAxis(xLsb, xMsb)/256.0);
    myLog.print("\t");
    myLog.print(readRawAxis(yLsb, yMsb)/256.0);
    myLog.print("\t");
    myLog.print(readRawAxis(zLsb, zMsb)/256.0);
    myLog.print("\t");
    myLog.print(millis());
  }
}
