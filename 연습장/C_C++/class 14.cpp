#include <stdio.h>

int main() {
	int num;

	again: // goto�� ���� ������ üũ����Ʈ

	printf("\n1. New Game\n");
	printf("\n2. Load Game\n");
	printf("\n3. Setting\n");
	printf("\n4. Credit\n");

	printf("\n��ȣ�� �����ϼ���. >> ");
	scanf_s("%d", &num);

	switch (num) { // ���ӵ� if, else if�� ����� �ڵ�
	case 1:
		printf("\nNew Game\n");

		printf("\nPlease waiting for first setting\n");
		break; // break ���� ������ �Ǹ� �ش� �ڵ尡 ����

	case 2:
		printf("\nLoad Game\n");
		printf("\nSlot 1\n");
		printf("\nSlot 2\n");
		printf("\nSlot 3\n");
		printf("\nSlot 4\n");

		int num1;

		printf("\n��ȣ�� �����ϼ���. >> ");
		scanf_s("%d", &num1);

		if (num1 == 1) {
			printf("\nPlease waiting for loarding saved game\n");
		}
		else if (num1 == 2) {
			printf("\nPlease waiting for loarding saved game\n");
		}
		else if (num1 == 3) {
			printf("\nPlease waiting for loarding saved game\n");
		}
		else if (num1 == 4) {
			printf("\nPlease waiting for loarding saved game\n");
		}
		else {
			printf("\n�߸��� �Է°��Դϴ�.\n");
			goto again; // �ش� ���� ��µ� ��� goto�� ���� again���� �̵�
		}

		break;

	case 3:
		printf("\nSetting\n");
		printf("\nSound = 5\n");
		printf("\nBright = 5\n");
		printf("\nDisplay = Full HD\n");
		goto again; // �ش� ���� ��µ� ��� goto�� ���� again���� �̵�
		break;

	case 4:
		printf("\nThank you for playing\n");
		printf("\nBy.HHJ\n");
		printf("\nTo be continued...\n");
		break;

	default:
		printf("\n�߸��� �Է°��Դϴ�.\n");
		goto again; // �ش� ���� ��µ� ��� goto�� ���� again���� �̵�
		break;
	}
}