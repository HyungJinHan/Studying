#include <stdio.h>

int main() {
	printf("%d %d %d %d\n", sizeof(int), sizeof(char), sizeof(float), sizeof(double));

	int a; char b; float c; double d;

	printf("%d %d %d %d\n", sizeof(a), sizeof(b), sizeof(c), sizeof(d));

	// 결과 : 4(int - 4바이트) 1(char - 1바이트) 4(float - 4바이트) 8(double - 4바이트)
	// sizeof(x) : x의 크기를 알려줌
	// x : int, float 등등의 데이터타입, 변수의 이름이 들어감

	int a1 = 3.14;
	double b1 = 10;
	printf("%d, %f\n", a1, b1);
	// 결과 : 3, 10.000000
	// 실수를 정수형 변수에 담을 수 없음
	// 정수를 실수형 변수에 담을 수 있음

	int math = 90, korean = 95, english = 96;
	int sum = math + korean + english; // int형으로 지정
	double avg = sum / 3;
	printf("%f\n", avg);
	// 예상 : 93.666667 / 결과 : 93.000000
	
	// ↓ 정수 결과값을 실수로 만들기1 ↓

	int math1 = 90, korean1 = 95, english1 = 96;
	double sum1 = math1 + korean1 + english1; // double형으로 지정
	double avg1 = sum1 / 3;
	printf("%f\n", avg1);
	// 예상 : 93.666667 / 결과 : 93.666667
	
	// ↓ 정수 결과값을 실수로 만들기2 ↓

	int math2 = 90, korean2 = 95, english2 = 96;
	int sum2 = math2 + korean2 + english2;
	double avg2 = (double)sum2 / 3; // 임시로 double형으로 지정
	printf("%f\n", avg2);
	// 예상 : 93.666667 / 결과 : 93.666667

	double a2 = 50.5;
	int b2 = 10;
	double a2b2 = a2 / b2;
	printf("%f\n", a2b2);
	// 결과 : 5.050000
	// 실수 / 정수 = 실수

	double a3 = 100.5;
	double b3 = 20.5;
	double a3b3 = a3 / b3;
	printf("%f\n", a3b3);
	// 결과 : 4.902439
	// 실수 / 실수 = 실수

	int a4 = 100.5;
	int b4 = 50;
	double a4b4 = a4 / b4;
	printf("%f\n", a4b4);
	// 결과 : 2.000000
	// 정수 / 정수 = 정수

	// 그 외 (-, * 동일)
	// 정수 + 정수 = 정수
	// 정수 + 실수 = 실수 (실수의 데이터 크기가 더 크기때문에)
	// 실수 + 실수 = 실수
}
