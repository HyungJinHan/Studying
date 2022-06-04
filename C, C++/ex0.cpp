#include <stdio.h>
// stdio.h라는 파일을 포함하는 코드로 언어 사용에 필요한 것들을 모아둠

int main() {
	printf("%d + %d = %d\n", 100, 10, 110); // 결과 : 100 + 10 = 110

	printf("%f\n", 3.14); // 결과 : 3.140000

	printf("%.2f\n", 3.141592); // 결과 : 3.14

	printf("%g\n", 3.141592); // 결과 : 3.14159

	printf("%.3g\n", 150.12154215); // 결과 : 150

	printf("%c %c %c\n", 'a', 'b', 'c'); // 결과 : a b c

	printf("%s\n", "Hello World"); // 결과 : Hello World
}
// C언어에서의 ()는 함수를 의미
// %d : 정수 / %f(.2) : 실수(자리수) / %g(.3) / %c : 문자 / %s : 문자열