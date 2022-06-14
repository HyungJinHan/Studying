
public class Array {

	public static void main(String[] args) {
		
		String[] family = new String[4];
		// 4칸짜리 서랍장과 같음
		family[0] = "hsh"; // []안의 숫자는 index (색인)
		family[1] = "jhs"; // "jhs"는 element (원소)
		family[2] = "hhj1";
		family[3] = "hhj2";
		
		System.out.println(family[2]);
		System.out.println(family.length); // 배열의 수
		
	}

}

// 결과
// hhj1
// 4