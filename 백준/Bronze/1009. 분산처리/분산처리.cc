#include <stdio.h>
int main() {
    int a = 0,b=0,c=0;
    scanf("%d", &a);
    
    for (int i = 0; i < a; i++) {
        int qwer = 1;
        scanf("%d %d", &b, &c);
        for (int j = 0; j < c; j++) {
            qwer = (qwer * b) % 10;
        }
        if (qwer == 0) {
            printf("10\n");
        }
        else {
            printf("%d\n", qwer);
        }
    }
    return 0;
}