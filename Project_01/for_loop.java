
public class for_loop {

	public static void main(String[] args) {
		
		// 출력값을 5번 반복
		for(int i = 1; i < 6; i++) {
			System.out.println("This is Loop_for "+"("+i+")");
			// 결과
			// This is Loop_for (1)
			// This is Loop_for (2)
			// This is Loop_for (3)
			// This is Loop_for (4)
			// This is Loop_for (5)
		}
		
		System.out.print("\n");
		
		// 21부터 57까지 출력 (오름차 순으로)
		for(int i = 21; i <= 57; i++) {
			System.out.print(i+" ");
			// 결과 : 21 ~ 57 (i++ : 1씩 올라감)
		}
		
		System.out.println("\n");
		
		// 96부터 53까지 출력 (내림차 순으로)
		for(int i = 96; i >= 53; i--) {
			System.out.print(i+" ");
			// 결과 : 96 ~ 53 (i-- : 1씩 내려감)
		}
		
		System.out.println("\n");
		
		// 21부터 57까지의 범위에서 홀수만 출력
		for(int i = 21; i <= 57; i = i + 2) {
			System.out.print(i+" ");
			// 결과 : 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57
			// i = i + 2 : 21부터 시작해서 2를 더해가며 홀수만 출력
		}

	}

}