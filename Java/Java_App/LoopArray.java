
public class LoopArray {

	public static void main(String[] args) {
		
		String[] family = new String[4];
		// 4칸짜리 서랍장과 같음
		family[0] = "hsh"; // []안의 숫자는 index (색인)
		family[1] = "jhs"; // "jhs"는 element (원소)
		family[2] = "hhj1";
		family[3] = "hhj2";
		
		for (int i = 0; i < family.length; i++) {
		// i < family.length를 통해 for문의 종료 시점을 유동적으로 변경 가능
			System.out.println("< "+family[i]+" >");
		}
		
	}

}

// 결과
// < hsh >
// < jhs >
// < hhj1 >
// < hhj2 >
