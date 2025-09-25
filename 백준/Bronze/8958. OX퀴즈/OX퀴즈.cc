#include <stdio.h>
int main() {
	int a = 0;
	scanf("%d", &a);
	char answer[81];
	for (int i = 0; i < a; i++) {
		int sum = 0;
		int count = 0;
		scanf("%s", answer);
		for (int j = 0; answer[j] != '\0'; j++) {
		if (answer[j] == 'O') {
			sum += 1;
			count += sum;
		}
		else{
			sum = 0;
		}
		}
	printf("%d\n", count);
	}
	return 0;
}