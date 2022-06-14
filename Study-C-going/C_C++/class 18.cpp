#include <stdio.h>

int main() {
	// ===== break 예제 ======
	for (int i = 1; ; i++) {
		int n;
		printf("\n숫자를 입력하세요.(0 나오면 종료) >> ");
		scanf_s("%d", &n);

		if (n == 0) {
			break;
			// n의 입력값이 0일 경우 즉시 반복문 종료
		}

		printf("\n%d번째 : %d\n", i, n);
	}

	// ====== continue 예제 ======
	int n;
	printf("\n숫자를 입력하세요.(3의 배수 제외 더하기) >> ");
	scanf_s("%d", &n);

	int sum = 0;

	for (int i = 1; i <= n; i++) {
		if (i % 3 == 0) {
		// 3으로 나눈 나머지가 0일 시(= 3의 배수일 시)
			continue;
			// 해당 조건일 시, 건너뜀
		}
		sum += i;
	}
	printf("%d\n", sum);
	// 결과 : 10 입력 시, 1+2+4+5+7+8+10=37

	// ====== 중첩 for문 예제1 ======
	int n1;
	printf("\n숫자를 입력하세요.(# 정사각형) >> ");
	scanf_s("%d", &n1);

	for (int i = 1; i <= n1; i++) {
		for (int j = 1; j <= n1; j++) {
			printf("# ");
		}
		printf("\n");
	}
	// 내부의 for문을 통해 # 을 입력한 n1만큼 출력 후,
	// 밖의 for문을 통해 줄바꿈
	// 위의 동작(n1만큼 # 출력 - 줄바꿈)을 n1만큼 반복
	// 결과 : 10 입력 시, 10X10 # 정사각형

	// ====== 중첩 for문 예제2 ======
	int n2;
	printf("\n숫자를 입력하세요.(# 계단) >> ");
	scanf_s("%d", &n2);

	for (int i = 1; i <= n2; i++) {
		for (int j = 1; j <= i; j++) {
		// j가 i보다 작거나 같을 때
			printf("# ");
		}
		printf("\n");
	}
	// 내부의 for문을 통해 # 을 i(1~)만큼 출력 후,
	// 밖의 for문을 통해 줄바꿈
	// 위의 동작(i만큼 # 출력 - 줄바꿈)을 n1만큼 반복
	// 결과 : 10 입력 시, 1~10까지의 # 계단
}