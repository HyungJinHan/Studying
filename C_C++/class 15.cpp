#include <stdio.h>

int main() {
	// while 반복문
	int i = 1;
	while (i <= 10) {
		printf("%d ", i);
		i++;
	}
	// 결과 : 1 2 3 4 5 6 7 8 9 10

	printf("\n\n");

	// do-while 반복문
	int i1 = 10;
	// i1의 숫자가 i1 <= 10에 해당되지 않더라도 1번은 코드를 실행해줌
	do {
		printf("%d ", i1);
		i1++;
	} while (i1 <= 10);
	// 결과 : 10

	printf("\n\n");

	int n;
	do {
		printf("비밀번호를 입력하세요.(1210) >> ");
		scanf_s("%d", &n);
	} while (n != 1210);
	// 1210이 아닌 경우, 계속해서 반복문 실행

	printf("\n비밀번호를 입력하셨습니다.\n");
	// 1210을 입력하면 비밀번호를 입력하셨습니다. 출력
}