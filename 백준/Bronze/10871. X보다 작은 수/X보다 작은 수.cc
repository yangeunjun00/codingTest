#include <stdio.h>
int main() {
	int a, b,x;
	scanf("%d %d", &a, &b);
	for (int i = 0; i < a; i++) {
		scanf("%d ", &x);
		if (x < b)
			printf("%d ", x);
	}
	return 0;


}