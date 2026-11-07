#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint32_t t = 0;
    while (1) {
        uint8_t left = (uint8_t)((t * 5 & t >> 7) | (t * 3 & t >> 10));
        uint8_t right = (uint8_t)((t * 5 & t >> 7) | (t * 11 & t >> 11));

        if (putchar(left) == EOF || putchar(right) == EOF) {
            break;
        }
        t++;
    }
    return 0;
}