#include <stdio.h>

int main() {
	int n;
	printf("숫자를 입력하세요. >> ");
	scanf_s("%d", &n);

	// n이 짝수일 시 n % 2 == 0이므로 true 값으로 출력
	// n이 홀수일 시 n % 2 != 0이므로 false 값으로 출력
	if (n % 2 == 0) {
		printf("\n입력한 n(%d)은 짝수입니다.\n", n);
	}
	else {
		printf("\n입력한 n(%d)은 홀수입니다.\n", n);
	}

	// n이 짝수일 시 n % 2의 값은 0이므로 false 값으로 출력
	// n이 홀수일 시 n % 2의 값은 1이므로 true 값으로 출력
	if (n % 2) {
		printf("\n입력한 n(%d)은 홀수입니다.\n", n);
	}
	else {
		printf("\n입력한 n(%d)은 짝수입니다.\n", n);
	}

	// else if문
	// n > 0이면 양수이므로 true 값으로 출력
	// n == 0이면 0이므로 else if의 true 값으로 출력
	// n < 0이면 음수이므로 else if의 false 값으로 출력
	if (n > 0) {
		printf("\n입력한 n(%d)은 양수입니다.\n", n);
	}
	else if (n == 0) {
		printf("\n입력한 n(%d)은 0입니다.\n", n);
	}
	else {
		printf("\n입력한 n(%d)은 음수입니다.\n", n);
	}
}