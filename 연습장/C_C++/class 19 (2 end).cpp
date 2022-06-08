#include <stdio.h>

int main() {
	// ===== ���� �Է� ��, �ش� ���� ��� =====
	int score;
	printf("������ �Է��ϼ���. >> ");
	scanf_s("%d", &score);

	if (score > 100 || score < 0) {
		printf("\n�߸��� ���� �Է��Դϴ�.");
	}
	else if (score >= 90) {
		printf("\nA ���� �Դϴ�.");
	}
	else if (score >= 80) {
		printf("\nB ���� �Դϴ�.");
	}
	else if (score >= 70) {
		printf("\nC ���� �Դϴ�.");
	}
	else if (score >= 60) {
		printf("\nD ���� �Դϴ�.");
	}
	else {
		printf("\nE ���� �Դϴ�.");
	}

	// ===== �ڿ��� �Է� ��, �ش� �ڿ����� ��� ��� =====
	int num;
	printf("\n\n�ڿ����� �Է��ϼ���. >> ");
	scanf_s("%d", &num);

	for (int i = 1; i <= num / 2; i ++) {
		if (num % i == 0) {
			printf("%d, ", i);
		}
	}
	printf("%d", num);
	// ������ ��°��� , ���ֱ�
	// �Է°��� �ڿ����� �������� ���� �� ������ ���� ���� ���

	// ===== 1�� �ڸ����� 3, 6, 9�� ��� # ��� =====
	int game;
	printf("\n\n������ ���� ���ڸ� �Է��ϼ���. >> ");
	scanf_s("%d", &game);

	for (int i = 1; i <= game; i++) {
		int k = i % 10;
		// i�� 10���� ���� �������� k��� ������ ���� (1�� �ڸ��� ǥ��)
		if (k == 3 || k == 6 || k == 9) {
			printf("# ");
		}
		else {
			printf("%d ", i);
		}
	}

	// ===== �Է°��� ���� Ȧ�� ��� ����� =====
	int stairs;
	printf("\n\n��� �� ���� �Է��ϼ���. >> ");
	scanf_s("%d", &stairs);

	for (int i = 1; i <= stairs; i++) {
		for (int j = 1; j <= i; j++) {
			printf("%d ", 2 * j - 1);
			// %d �� 2*1-1=1, 2*2-1=3, 2*3-1=5, 2*4-1=9...
		}
		printf("\n");
	}

	// ===== �Է°��� ���� ��� ���ڰ� 2���� �þ�� ��� ����� =====
	int stairs1;
	printf("\n\n��� �� ���� �Է��ϼ���. >> ");
	scanf_s("%d", &stairs1);

	for (int i = 0; i <= stairs1; i++) {
		for (int j = 1; j <= i * 2 + 1; j++) {
		// i��° �ٿ��� ��µǴ� ������ ���� : 2*i-1 (2*1-1=1, 2*2-1=3, 2*3-1=5...)
			printf("%d ", j);
		}
		printf("\n");
	}
}