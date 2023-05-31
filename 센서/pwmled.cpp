#define USING_DHT11 true // The DHT11 uses only 8 bits
#define DHT_GPIO 22 // Using GPIO 22 for this example
#define LH_THRESHOLD 26

int main() {
    int humid = 0, temp = 0;
    cout << "start "<< endl;
    wiringPiSetupGpio();
    piHiPri(99);

    TRYAGAIN :
    static unsigned char data[5] = { 0,0,0,0,0};
    pinMode(DHT_GPIO,OUTPUT);
    digitalWrite(DHT_GPIO,LOW);
    usleep(18000);
    digitiaWrite(DHT_GPIO,HIGH);
    pinMode(DHT_GPIO,INPUT);

    do{delayMicriseconds(1);} while(digitalRead(DHT_GPIO) == HIGH);
    do{delayMicriseconds(1);} while(digitalRead(DHT_GPIO) == LOW);
    do{delayMicriseconds(1);} while(digitalRead(DHT_GPIO) == HIGH);

    for(int d=0; d<5; d++) {
        for(int i=0; i<8; i++){
             do{delayMicriseconds(1);} while(digitalRead(DHT_GPIO) == LOW);
             int width = 0;
             do {
                width++;
                delayMicroSeconds(1);
                if(width>1000) break;
             } while(digitalRead(DHT_GPIO) == HIGH);
             data[d] = data[d] | ((width > LH_THRESHOLD) << (7-i)); 
        }
    }
    if(USING_DHT11) {
        humid = data[0] * 10;
        temp = data[2] * 10;
    }

}
