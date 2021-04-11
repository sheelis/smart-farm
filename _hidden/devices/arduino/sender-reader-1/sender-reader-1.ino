

String inputString = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete

int i=0;
int rx=0;

#define sensorpin A7
#define ledpin 2

void setup() {
  pinMode(sensorpin, INPUT);
  pinMode(ledpin, OUTPUT);
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    if(inputString == "version\n"){
        Serial.println("greenhouse1");
    } else if(inputString == "on\n"){
        digitalWrite(ledpin, HIGH);
    } else if(inputString == "off\n"){
        digitalWrite(ledpin, LOW);
    } else {
      Serial.print("tingbudong:");
      Serial.print(inputString);
    }
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
  i = analogRead(sensorpin);
  Serial.println(i);
  delay(1000);
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
