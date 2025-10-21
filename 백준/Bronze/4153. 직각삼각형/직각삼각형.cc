#include <stdio.h>
int main() {
	int n = 1;
	int a = 1;
	int b = 1;
	while (1) {
		scanf("%d %d %d", &n, &a, &b);
		if (n == 0 && b == 0 && a == 0)break;
		int max = (n > a) ? ((n > b) ? n : b) : ((a > b) ? a : b);
		int min = (n < a) ? ((n < b) ? n : b) : ((a < b) ? a : b);
		if (max * max == (n + a + b - max-min) * (n + a + b - max - min) + min*min) {
			printf("right\n");
		}
		else  {
			printf("wrong\n");
		}
	}
	return 0;
}