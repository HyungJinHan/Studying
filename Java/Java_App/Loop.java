
public class Loop {

	public static void main(String[] args) {
		
		System.out.println(1);
		
		System.out.println("===== while =====");
		int i = 0;
		while (i < 3) {
			i++; // == i = i + 1;
			System.out.println(2);
			System.out.println(3);
		}
		
		System.out.println("===== for =====");
		for(int i1 = 0; i1 < 4; i1++) {
			System.out.println(2);
			System.out.println(3);
		}
		
		System.out.println(4);

	}

}

// 결과
// 1
// ===== while (i < 3) =====
// 2 (0)
// 3
// 2 (1)
// 3
// 2 (2 - i < 3으로 인해 종료)
// 3
// ===== for (i1 < 4) =====
// 2 (0)
// 3
// 2 (1)
// 3
// 2 (2)
// 3
// 2 (3 - i1 < 4으로 인해 종료)
// 3
// 4