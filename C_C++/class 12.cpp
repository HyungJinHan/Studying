#include <stdio.h>

int main() {
	int n;
	printf("���ڸ� �Է��ϼ���. >> ");
	scanf_s("%d", &n);

	// n�� ¦���� �� n % 2 == 0�̹Ƿ� true ������ ���
	// n�� Ȧ���� �� n % 2 != 0�̹Ƿ� false ������ ���
	if (n % 2 == 0) {
		printf("\n�Է��� n(%d)�� ¦���Դϴ�.\n", n);
	}
	else {
		printf("\n�Է��� n(%d)�� Ȧ���Դϴ�.\n", n);
	}

	// n�� ¦���� �� n % 2�� ���� 0�̹Ƿ� false ������ ���
	// n�� Ȧ���� �� n % 2�� ���� 1�̹Ƿ� true ������ ���
	if (n % 2) {
		printf("\n�Է��� n(%d)�� Ȧ���Դϴ�.\n", n);
	}
	else {
		printf("\n�Է��� n(%d)�� ¦���Դϴ�.\n", n);
	}

	// else if��
	// n > 0�̸� ����̹Ƿ� true ������ ���
	// n == 0�̸� 0�̹Ƿ� else if�� true ������ ���
	// n < 0�̸� �����̹Ƿ� else if�� false ������ ���
	if (n > 0) {
		printf("\n�Է��� n(%d)�� ����Դϴ�.\n", n);
	}
	else if (n == 0) {
		printf("\n�Է��� n(%d)�� 0�Դϴ�.\n", n);
	}
	else {
		printf("\n�Է��� n(%d)�� �����Դϴ�.\n", n);
	}
}