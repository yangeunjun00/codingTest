#include <stdio.h>
int main() {
	int t;
	int h = 0;
	int w = 0;
	int n = 0;
	scanf("%d", &t);	
	int sum[1000] = { 0 };
	for (int i = 0; i < t; i++) {
		scanf("%d %d %d", &h, &w, &n);
		if (n % h == 0) {
			sum[i] = h * 100 + n / h;
		}
		else
			sum[i] = (n % h) * 100 + (n / h) + 1;
	}
	for (int i = 0; i < t; i++) {
		printf("%d\n", sum[i]);

	}
	return 0;
}