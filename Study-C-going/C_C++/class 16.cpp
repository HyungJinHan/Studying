#include <stdio.h>

int main() {
	// ===== 예제 1 =====
	int i;
	// for문 밖에서 i라는 변수를 지정

	for (i = 1; i <= 10; i++) {
		printf("%d ", i);
	}
	// 결과 : 1 2 3 4 5 6 7 8 9 10
	// for문의 밖에서 i라는 변수를 정의하면 for문의 밖에서도 i를 사용

	// ===== 예제 2 =====
	int n;
	printf("\n\n숫자를 입력하세요. >> ");
	scanf_s("%d", &n);

	for (int i = 1; i <= n; i *= 2) {
	// for문 내에서 i라는 변수를 지정
		printf("%d ", i);
	}
	// 결과 : 100 입력 시, 1 2 4 8 16 32 64
	// for문의 안에서 i라는 변수를 정의하면 같은 i라는 변수라도 재사용 가능

	// ===== 예제 3 =====
	int f;
	printf("\n\n숫자를 입력하세요. >> ");
	scanf_s("%d", &f);
	// 입력할 값을 지정

	int sum = 0;
	// sum이라는 변수를 0으로 지정

	for (int i = 1; i <= f; i++) {
		sum += i;
		// i가 1씩 증가하면서 sum이라는 변수에 i를 더하고
		// 입력값과 같아지면 반복문 종료
	}
	printf("%d ", sum);
	// 결과 : 100 입력 시, 5050

	// ===== 예제 4 =====
	int e;
	printf("\n\n숫자를 입력하세요. >> ");
	scanf_s("%d", &e);

	for (int i = 1; i <= e; i++) {
		printf("* ");
	}
}