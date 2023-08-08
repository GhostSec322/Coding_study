#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void) {
	int arr[3] = { 1,2,3 };
	for (int i = 0; i < sizeof(arr)/sizeof(int); i++) {
		printf("%d \n", arr[i]);
	}
	char name[] = "Kim Min Soub";
	for (int i = 0; i < sizeof(name) / sizeof(char); i++) {
		printf("%c", name[i]);
	}
	return 0;
}