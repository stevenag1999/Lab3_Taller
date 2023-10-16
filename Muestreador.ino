/*
 * Pines y Variables
 */
int cant_canales = 0;
byte escala = 0;
byte escala2 = 0;
byte ch1 = 0;
byte ch2 = 0;



/*
 * Configuración Inicial y General
 */
void setup() {
    //Iniciar Comunicación serial
    Serial.begin(115200);
  
    // Configuración General del ADC
    //->Registro ADMUX
    ADMUX |= (1 << REFS0); //Voltaje de referencia 5V (REFS1 ya está en 0)
    ADMUX |= (1 << ADLAR); //Ajuste Izquierdo
    //->Registro ADCSRA
    ADCSRA |= (1 << ADATE); // Free-running
    ADCSRA |= (1 << ADIE); // habilitar interrupciones del ADC
  
    ADCSRA &= ~(1 << ADPS2) & ~(1 << ADPS1) & ~(1 << ADPS0);    //Prescaler en 2
  
    sei(); // Habilita las interrupciones globales
  
    // Pines para las escalas
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
}






/*
 * Main del Programa
 */
void loop() {
    //-------------------------------------------------------------------------
    //Primero revisar si la compu ha enviado algo
    if (Serial.available() > 0) {
      byte comando = Serial.read();  // Recibir la instrucción
      ch1 = comando & 0b00000001;  // bit para el estado del canal 1
      ch2 = (comando>>1) & 0b00000001;  // bit para el estado del canal 2
      escala = (comando >> 2) & 0b00000111;   // Bits 2, 3 y 4 para la escala
      escala2 = (comando >> 5) & 0b00000111;  // Bits 5, 6 y 7 para la escala 2
      if (ch1==0 && ch2==0) {
        cant_canales = 0; // apagar los dos canales
      } else if ((ch1==1 && ch2==0) || (ch1==0 && ch2==1)) {
        cant_canales = 1;
      } else if (ch1==1 && ch2==1) {
        cant_canales = 2;
      }
    }


    //-------------------------------------------------------------------------
    //Editar escala del DAS
    switch (escala) {
      case 0: //Escala 0: 10 mV
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        digitalWrite(2, HIGH);
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
        break;
      case 1: //Escala 1: 100mV
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        digitalWrite(2, LOW);
        digitalWrite(3, HIGH);
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
        break;
      case 2: //Escala 2: 1V
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
        digitalWrite(4, HIGH);
        digitalWrite(5, LOW);
        break;
      case 3: //Escala 3: 2.5V
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);
        digitalWrite(5, HIGH);
        break;
      case 4: //Escala 4: 5V
        digitalWrite(6, HIGH);
        digitalWrite(7, LOW);
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
        break;
      case 5: //Escala 5: 10V
        digitalWrite(6, LOW);
        digitalWrite(7, HIGH);
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
        break;
      /*
      default:
        digitalWrite(2, HIGH);
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        break;
      */
    }





    //-------------------------------------------------------------------------
    //Mayor jerarquía: canales apagos
    if(cant_canales == 0){
      ADCSRA &= ~(1 << ADEN);  //Apago el adc 
    } 
  
  
  
    
    else {
        ADCSRA |= (1 << ADEN);  //Enciendo el adc 
        
        if (cant_canales == 1){   //Segunda jerarquía: la velocidad
          if (ch1 == true){ //Para el canal 1
            ADMUX &= ~(1 << MUX0); //Escojo el canal 1 (ADC0) (MUX[3:0]=0000)
            ADCSRA |= (1 << ADSC);  //Arranco la conversión
          }
          if (ch2 == true) {  //Para el canal 2
            ADMUX |= (1 << MUX0); //Escojo el canal 2 (ADC1) (MUX[3:0]=0001)
            ADCSRA |= (1 << ADSC);  //Arranco la conversión
          }
        }
  
        /*
        else {    //Acción para alimentar los dos canales
          //ADCSRA |= (1 << ADPS2) | (1 << ADPS1); // Prescaler en 64
          //ADCSRA &= ~(1 << ADPS0);
          if (ch1 == true){ //Para el canal 1
            ADMUX &= ~(0b00000001);  //Canal 0 del MUX del ADC
            ADCSRA |= (0b01000000);  //Arracar conversiones
            delay(1);
          }if (ch2 == true){  //Para el canal 2
            ADMUX |= (0b00000001);  //Canal 1 del MUX del ADC
            ADCSRA |= (0b01000000);  //Arracar conversiones
          }
        }
        */

        
    }

  //delay(1);
}








/*
 * Interrupción de Conversión Concluida
 */
ISR(ADC_vect) {
  int dato = ADCH;
  Serial.println(dato);
}





