/*#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
	// if문 : 내부조건을 검사해 프로그램의 진행경로를 결정, 조건이 많지 않을때 사용하는 것이 유리하다
	printf("손님이 몇명 왔나요:");
	int client = 0;
	scanf("%d", &client);
	if (client == 1 || client == 2) {
		printf("2인석으로 안내합니다.\n");
	}
	else if (client == 3 || client == 4) {
		printf("4인석으로 안내합니다.\n");
	}
	else {
		printf("대형석으로 안내합니다\n");
	}
	// switch문 다양한 조건이 존재할때 사용함
	switch (client) {
	case 1:
	case 2: printf("2인석으로 안내합니다");
		break;
	case 3:
	case 4: printf("4인석으로 안내합니다");
		break;
	default:
		printf("대형석으로 안내합니다");
	}
	return 0;
}*/