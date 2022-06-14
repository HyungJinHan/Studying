#include <stdio.h>

int main() {
	int num;

	again: // goto를 위한 일종의 체크포인트

	printf("\n1. New Game\n");
	printf("\n2. Load Game\n");
	printf("\n3. Setting\n");
	printf("\n4. Credit\n");

	printf("\n번호를 선택하세요. >> ");
	scanf_s("%d", &num);

	switch (num) { // 연속된 if, else if와 비슷한 코드
	case 1:
		printf("\nNew Game\n");

		printf("\nPlease waiting for first setting\n");
		break; // break 값이 실행이 되면 해당 코드가 종료

	case 2:
		printf("\nLoad Game\n");
		printf("\nSlot 1\n");
		printf("\nSlot 2\n");
		printf("\nSlot 3\n");
		printf("\nSlot 4\n");

		int num1;

		printf("\n번호를 선택하세요. >> ");
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
			printf("\n잘못된 입력값입니다.\n");
			goto again; // 해당 값이 출력된 경우 goto를 통해 again으로 이동
		}

		break;

	case 3:
		printf("\nSetting\n");
		printf("\nSound = 5\n");
		printf("\nBright = 5\n");
		printf("\nDisplay = Full HD\n");
		goto again; // 해당 값이 출력된 경우 goto를 통해 again으로 이동
		break;

	case 4:
		printf("\nThank you for playing\n");
		printf("\nBy.HHJ\n");
		printf("\nTo be continued...\n");
		break;

	default:
		printf("\n잘못된 입력값입니다.\n");
		goto again; // 해당 값이 출력된 경우 goto를 통해 again으로 이동
		break;
	}
}