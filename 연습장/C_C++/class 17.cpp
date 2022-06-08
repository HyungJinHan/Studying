#include <stdio.h>

int main() {
	int i;
	printf("숫자를 입력하세요. >> ");
	scanf_s("%d", &i);
	// for문은 외부에서 변수를 지정하고
	// for문 내의 초기 변수를 지정하지 않아도 작동 가능

	for (; i <= 10; i++) {
	// 조건(i <= 10)가 비어있다면 true로 간주
		printf("%d ", i);
	}

	int n;
	printf("\n숫자를 입력하세요. >> ");
	scanf_s("%d", &n);

	int f = 0, t = 1;

	while (f <= n) {
		printf("2^%d = %d\n", f, t);
		f++;
		t *= 2;
	}
	// 결과 : 2 입력 시, 2^0 = 1 / 2^1 = 2 / 2^2 = 4

	// ↓ while문과 for문의 비교 ↓

	int c;
	printf("\n숫자를 입력하세요. >> ");
	scanf_s("%d", &c);

	for (int a = 0, b = 1; a <= c; a++, b *= 2) {
	// for문의 ()에 변수 지정과 연산을 여러개 넣을 수 있음
		printf("2^%d = %d\n", a, b);
	}
	// 2^0(a = 0) = 1(b = 1)
	// 2^1(a++) = 2(b *= 2)
	// 결과 : 2 입력 시, 2^0 = 1 / 2^1 = 2 / 2^2 = 4

	int i1, sum;
	for (i1 = 1, sum = 0; i1 <= c; sum += i1, i1++);
	// for문의 {}내의 내용이 없다면 지워도 무방 (; 필수)
	printf("\n1~%d의 합 = %d", c, sum);
	// 결과 : 2 입력 시, 1 + 2 = 3
}