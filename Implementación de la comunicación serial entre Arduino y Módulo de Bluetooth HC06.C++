float sinVal;
int toneVal;
void setup(){
  pinMode(9, OUTPUT); // Definimos el pin 9 como salida.
  Serial.begin( 9600 );    // 9600 es el valor por defecto para la coneccion bluetooth
}
void loop() {
  // recibir datos
  while ( Serial.available() > 0 ) {
    // lectura de números desde el puerto serial
    //count es  la variable donde se almacena el valor recibido
    int count = Serial.parseInt();
     // presentar los número recibidos
    while (count > 0) {
        Serial.print("DATOS RECIBIDOS: ");
        Serial.println(String(count));
          for(int x=0; x<180; x++){
      // convertimos grados en radianes para luego obtener el valor.
           sinVal = (sin(x*(3.1412/180)));
      // generar una frecuencia a partir del valor sin
          toneVal = 2000+(int(sinVal*1000));
          tone(9, toneVal);
          delay(2);
    }
  }
  }
}
