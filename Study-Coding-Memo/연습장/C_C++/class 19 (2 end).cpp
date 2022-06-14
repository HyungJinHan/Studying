#include <stdio.h>

int main() {
	// ===== 점수 입력 시, 해당 학점 출력 =====
	int score;
	printf("점수를 입력하세요. >> ");
	scanf_s("%d", &score);

	if (score > 100 || score < 0) {
		printf("\n잘못된 점수 입력입니다.");
	}
	else if (score >= 90) {
		printf("\nA 학점 입니다.");
	}
	else if (score >= 80) {
		printf("\nB 학점 입니다.");
	}
	else if (score >= 70) {
		printf("\nC 학점 입니다.");
	}
	else if (score >= 60) {
		printf("\nD 학점 입니다.");
	}
	else {
		printf("\nE 학점 입니다.");
	}

	// ===== 자연수 입력 시, 해당 자연수의 약수 출력 =====
	int num;
	printf("\n\n자연수를 입력하세요. >> ");
	scanf_s("%d", &num);

	for (int i = 1; i <= num / 2; i ++) {
		if (num % i == 0) {
			printf("%d, ", i);
		}
	}
	printf("%d", num);
	// 마지막 출력값에 , 없애기
	// 입력값인 자연수의 절반으로 나눈 후 마지막 값만 따로 출력

	// ===== 1의 자릿수가 3, 6, 9인 경우 # 출력 =====
	int game;
	printf("\n\n게임을 위한 숫자를 입력하세요. >> ");
	scanf_s("%d", &game);

	for (int i = 1; i <= game; i++) {
		int k = i % 10;
		// i를 10으로 나눈 나머지를 k라는 변수로 지정 (1의 자리를 표현)
		if (k == 3 || k == 6 || k == 9) {
			printf("# ");
		}
		else {
			printf("%d ", i);
		}
	}

	// ===== 입력값에 따른 홀수 계단 만들기 =====
	int stairs;
	printf("\n\n계단 층 수를 입력하세요. >> ");
	scanf_s("%d", &stairs);

	for (int i = 1; i <= stairs; i++) {
		for (int j = 1; j <= i; j++) {
			printf("%d ", 2 * j - 1);
			// %d → 2*1-1=1, 2*2-1=3, 2*3-1=5, 2*4-1=9...
		}
		printf("\n");
	}

	// ===== 입력값에 따른 출력 숫자가 2개씩 늘어나는 계단 만들기 =====
	int stairs1;
	printf("\n\n계단 층 수를 입력하세요. >> ");
	scanf_s("%d", &stairs1);

	for (int i = 0; i <= stairs1; i++) {
		for (int j = 1; j <= i * 2 + 1; j++) {
		// i번째 줄에서 출력되는 숫자의 개수 : 2*i-1 (2*1-1=1, 2*2-1=3, 2*3-1=5...)
			printf("%d ", j);
		}
		printf("\n");
	}
}