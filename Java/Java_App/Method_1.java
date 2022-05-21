
public class Method_1 {
	
	public static void main(String[] args) {
		System.out.println(printAll("hhj", ""));
		System.out.println(printAll("hsh", "---"));
		System.out.println(printAll("jhs", "==="));
	}
	
	public static String printAll(String name, String line) {
		String out = "";
		// out은 String이라는 것을 지정
		out = out + line + "\n";
		out = out + name + "\n";
		out = out + name;
		// printAll("name", "line")의 name과 line을 지정 시
		// 위의 정한 내용이 출력
		return out;
		// Method 종료
	}
	
}

// 결과
// hhj
// hhj
// ---
// hsh
// hsh
// ===
// jhs
// jhs