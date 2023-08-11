#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

// Convert one ASCII value to binary and store each bit in a cell of an array of type char. Then print the corresponding bulb for a bit
char *convert(int value);

// Print one emoji to represent one bulb on or off
void print_bulb(int bit);

char *convert(int value){
    char *bits = malloc(sizeof(char) * BITS_IN_BYTE), aux[BITS_IN_BYTE], bit;

    for (int i = 0; i < BITS_IN_BYTE; i++) {
        bit = value % 2;
        bits[i] = bit;
        value /= 2;
    }

    for (int i = 0; i < BITS_IN_BYTE; i++) {
        aux[BITS_IN_BYTE - 1 - i] = bits[i];
    }

    for (int i = 0; i < BITS_IN_BYTE; i++) {
        bits[i] = aux[i];
    }
    return bits;
}

void print_bulb(int bit){
    if (bit == 0){
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1){
        // Light emoji
        printf("\U0001F7E1");
    }
}

int main(void){
    char message[1024], *bits;
    printf("Message: ");
    for (int i = 0, n = strlen(message); i < n; i++) {
        bits = convert(message[i]);
        for (int j = 0; j < BITS_IN_BYTE; j++){
            print_bulb(bits[j]);
        }
        printf("\n");
    }
}