#define _CRT_SECURE_NO_WARNINGS
// 보안관련 이슈를 띄우지 말라는 코드 (ex : scanf 사용 시)

#include <stdio.h>

int main() {
	// 두 정수를 입력받아 그 정수들의 합 구하기
	int a, b;

	printf("첫번째 정수를 입력하세요. >> "); // 입력값 : 100
	scanf("%d", &a);
	printf("두번째 정수를 입력하세요. >> "); // 입력값 : 50
	scanf("%d", &b);

	printf("\n두 정수의 합은 %d입니다.\n", a + b); // 결과 : 150

	getchar(); // scanf가 무시되는 현상을 막는 입력버퍼 비우기 코드

	// 체중과 키를 입력받아 BMI(체질량) 지수 구하기 (BMI : 체중/키^2)
	float a1, b1;

	printf("\n키를 미터 단위로 입력하세요. >> "); // 입력값 : 1.8
	scanf("%f", &a1);
	printf("체중을 킬로그램 단위로 입력하세요. >> "); // 입력값 : 65
	scanf("%f", &b1);

	printf("\n당신의 BMI(체질량) 지수는 %f입니다.\n", b1 / (a1 * a1)); // 결과 : 20.061729

	getchar(); // scanf가 무시되는 현상을 막는 입력버퍼 비우기 코드

	// 알파벳을 입력받아 그 다음 알파벳 출력하기
	char a2;

	printf("\n알파벳을 입력하세요. >> "); // 입력값 : f
	scanf("%c", &a2);
	printf("\n입력한 알파벳 %c의 다음 알파벳은 %c입니다.\n", a2, a2 + 1); // 결과 : g
}