/*#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
	// if�� : ���������� �˻��� ���α׷��� �����θ� ����, ������ ���� ������ ����ϴ� ���� �����ϴ�
	printf("�մ��� ��� �Գ���:");
	int client = 0;
	scanf("%d", &client);
	if (client == 1 || client == 2) {
		printf("2�μ����� �ȳ��մϴ�.\n");
	}
	else if (client == 3 || client == 4) {
		printf("4�μ����� �ȳ��մϴ�.\n");
	}
	else {
		printf("���������� �ȳ��մϴ�\n");
	}
	// switch�� �پ��� ������ �����Ҷ� �����
	switch (client) {
	case 1:
	case 2: printf("2�μ����� �ȳ��մϴ�");
		break;
	case 3:
	case 4: printf("4�μ����� �ȳ��մϴ�");
		break;
	default:
		printf("���������� �ȳ��մϴ�");
	}
	return 0;
}*/