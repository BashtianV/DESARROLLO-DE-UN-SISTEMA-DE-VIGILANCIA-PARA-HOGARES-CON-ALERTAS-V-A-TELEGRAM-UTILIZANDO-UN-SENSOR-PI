float sinVal;
int toneVal;
 
void setup(){
    pinMode(8, OUTPUT); // Definimos el pin 8 como salida.
}
 
void loop(){
    for(int x=0; x<180; x++){
           // convertimos grados en radianes para luego obtener el valor.
           sinVal = (sin(x*(3.1412/180)));
           // generar una frecuencia a partir del valor sin
           toneVal = 2000+(int(sinVal*1000));
           tone(8, toneVal);
           delay(2);
     }   
}