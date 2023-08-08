/*#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
	int n = 0;
	int result = 0;
	printf("n을 입력하세요:");
	scanf("%d", &n);
	for (int i = 0; i <= n; i++) {
		result += i;
	}
	printf("%d", result);
	n = 0;
	char a;
	scanf("%d %c", &n,&a);
	while (n) {
		printf("%c \n", a);
		n--;
	}
	int c = 2;
	int d = 1;
	for (c; c <= 9; c++) {
		printf("%d 단 \n", c);
		for (d; d <= 9; d++) {
			printf("%d X %d =%d \n", c, d, c * d);
		}
		d = 1;
	}
	return 0;
}*/