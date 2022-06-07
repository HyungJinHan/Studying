#include <stdio.h>

int main() {
	int a; // 변수 선언 (integer)
	// 변수 가능 : 알파벳 대소문자, _, 숫자(a2 O / 2a X)

	a = 10; // a에 10을 대입
	printf("%d\n", a); // 결과 : 10

	a = 100; // a에 100을 대입
	printf("%d\n", a); // 결과 : 100

	int b = 50; // 변수 초기화
	int c = 150;
	int sum = b + c;
	printf("%d + %d = %d\n", b, c, sum);
}