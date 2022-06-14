#define _CRT_SECURE_NO_WARNINGS
// 보안관련 이슈를 띄우지 말라는 코드 (ex : scanf 사용 시)

#include <stdio.h>

int main() {

	char a = 67;
	// char : 1바이트 정수형 (int : 4바이트)
	// 문자 (반각문자가 들어옴 - A~Z, a~z, 0~9, 기타 특수문자)

	printf("%d\n", a); // 결과 : 67
	printf("%c\n", a); // 결과 : C (a안의 67이 C의 코드를 의미)
	printf("%c\n", 67); // 결과 : C (67번째 코드)
	printf("%d\n", 'C'); // 결과 : 67 (67번째 코드인 C)

	// ASCII 코드 : 문자를 숫자와 대응시키는 미국의 표준 코드

	char a1;
	
	printf("\n문자를 입력하세요. >> ");
	scanf("%c", &a1);
	printf("\n입력한 문자는 %c입니다.\n", a1);
	// 결과 : 입력한 문자가 그대로 출력
	printf("\n%c의 ASCII 값은 %d입니다.\n\n", a1, a1);
	// 결과 : %c에는 문자 그대로, %d는 해당 ASCII 값이 출력
	
	int a2;

	printf("\n0부터 127까지의 숫자를 입력하세요. >> ");
	scanf("%d", &a2);
	printf("\n입력한 숫자는 %d입니다.\n", a2);
	// 결과 : 입력한 숫자가 그대로 출력
	printf("\n%d의 ASCII 문자는 %c입니다.\n", a2, a2);
	// 결과 : %d에는 숫자 그대로, %c는 해당 ASCII 값이 출력
}
