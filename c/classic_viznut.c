#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint32_t t = 0;
    while (1) {
        uint8_t sample = (uint8_t)(t * ((t >> 12) | (t >> 8)) & 63 & (t >> 4));
        if (putchar(sample) == EOF) {
            break;
        }
        t++;
    }
    return 0;
}