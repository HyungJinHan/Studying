#include <stdio.h>

int main() {
	// 산술연산자
	// +, -, *, /, =, %, +=, -=, *=, /=, %=, ++, --

	int a;
	a = 100;
	printf("a는 원래 %d이었다.\n", a);

	a = a + 10;
	printf("a에 10을 더해서 %d이 되었다.\n", a);

	int b;
	b = 200;
	b += 20; // b = b + 20
	printf("\nb에 20을 더해서 %d이 되었다.\n", b);

	b *= 10; // b = b * 10
	printf("b에 10을 곱해서 %d이 되었다.\n", b);

	b -= 1000; // b = b - 1000
	printf("b에 1000을 빼서 %d이 되었다.\n", b);

	b %= 7; // b = b % 7
	printf("b를 7로 나눈 나머지는 %d이다.\n", b);

	int c;
	c = 50;
	printf("\nc는 %d이다.\n", c);
	c++; // c = c + 1, c += 1
	printf("c++의 결과는 %d이다.\n", c);

	int d;
	d = 30;
	printf("\nd는 %d이다.\n", d);
	d--; // d = d - 1, d -= 1
	printf("d--의 결과는 %d이다.\n", d);
}