#include <stdio.h>

int main() {
	int a, b;

	printf("a를 입력하세요. >> ");
	scanf_s("%d", &a);

	getchar(); // scanf가 무시되는 현상을 막는 입력버퍼 비우기 코드

	printf("b를 입력하세요. >> ");
	scanf_s("%d", &b);

	// Comparison Operator (비교 연산자) - Boolean : 참, 거짓
	bool p = a > b;
	bool p1 = a >= b;
	bool q = a < b;
	bool q1 = a <= b;
	bool r = a == b; // 같다
	bool r1 = a != b; // 다르다
	printf("%d\n", p);
	// 결과 : 0 false (a=5, b=10) / 0 false (a=5, b=5)
	printf("%d\n", p1);
	// 결과 : 0 false (a=5, b=10) / 1 true (a=5, b=5)
	printf("%d\n", q);
	// 결과 : 1 true (a=5, b=10) / 0 false (a=5, b=5)
	printf("%d\n", q1);
	// 결과 : 0 false (a=5, b=10) / 1 true (a=5, b=5)
	printf("%d\n", r);
	// 결과 : 0 false (a=5, b=10) / 1 true (a=5, b=5)
	printf("%d\n", r1);
	// 결과 : 1 true (a=5, b=10) / 0 false (a=5, b=5)

	// Logical Operator (논리 연산자)
	bool l = a >= 1 && a <= 10; // 그리고
	bool l1 = a >= 1 || a <= 10; // 또는
	bool l2 = !l1; // 반대 (true는 false, false는 true)
	printf("\n%d\n", l); // 0 false (a = 20)
	printf("%d\n", l1); // 1 true (a = 20)
	printf("%d\n", l2); // 0 false (l1 = true)
}