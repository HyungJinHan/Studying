
public class Method_output {

	public static void main(String[] args) {
				// void는 return값이 없다는 뜻
		System.out.println(str());
		System.out.println(num());
	}
	
	public static String str() {
	// return 값인 String(문자열)인 a를 a() 자리에 출력
		return "Welcome HHJ";
		// return은 Method가 종료됨
	}
	
	public static int num() {
	// return 값인 int(숫자)인 1를 a() 자리에 출력
		return 112233;
	}

}

// 결과
// Welcome HHJ
// 112233