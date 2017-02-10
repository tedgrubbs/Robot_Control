
const int forward = 3;
const int backward = 6;
const int left = 9;
const int right = 12;

void turnOnMotor(const int dir)//moves motors. Right now it just turns on some LEDs
{
  digitalWrite(dir, HIGH);
  delay(200);
  digitalWrite(dir, LOW);
}

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(forward, OUTPUT);
  pinMode(backward, OUTPUT);
  pinMode(left, OUTPUT);
  pinMode(right, OUTPUT);
}

void loop() {
  // if there's any serial available, read it:
  while (Serial.available() > 0) {

      char input = char(Serial.read());

      Serial.println(input);

      switch(input)
      {
        case 'f' : turnOnMotor(forward);
                   break;
        case 'b' : turnOnMotor(backward);
                   break;
        case 'l' : turnOnMotor(left);
                   break;
        case 'r' : turnOnMotor(right);
                   break;                      
      }
    }
  }









