char myChar;
float sinVal;
int toneVal;
void setup(){
  pinMode(8, OUTPUT); // Definimos el pin 9 como salida.
  Serial.begin(9600);    // 9600 es el valor por defecto para la coneccion bluetooth
}
void loop() {
  // recibir datos
while ( Serial.available()>0)
  {
     myChar = Serial.read();
   while (myChar='a')
       {  // activacion de la alarma
          for(int y=0; y<15; y++){
          for(int x=0; x<180; x++){
      //          convertimos grados en radianes para luego obtener el valor.
                  sinVal = (sin(x*(3.1412/180)));
      // generar una frecuencia a partir del valor sin
                  toneVal = 2000+(int(sinVal*1000));
                  tone(8, toneVal);
                 delay(2) ;
         
          }
         
          }
       }
  }
}
