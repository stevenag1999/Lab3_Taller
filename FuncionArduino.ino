void setup() {
  // Inicialización del puerto serie
  Serial.begin(9600);
}

void loop() {
  // Valor aleatorio para prueba
  int dato = random(0, 1024);

  // Enviar el valor aleatorio a través del puerto serie
  Serial.println(dato);

  delay(250); // BW del dispositivo???
}

