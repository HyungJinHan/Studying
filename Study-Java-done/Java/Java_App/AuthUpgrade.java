
public class AuthUpgrade {

	public static void main(String[] args) {
		
		String[][] family = {
				{"hsh", "1111"},
				{"jhs", "2222"},
				{"hhj1", "3333"},
				{"hhj2", "4444"}
		};
		// id와 pw를 하나의 배열로 표현
		// 배열 내의 배열을 [][]로 처리해서 사용 가능
		
		String inputId = args[0];
		// id값
		String inputPW = args[1];
		// pw 값
		
		boolean isLogin = false;
		for(int i = 0; i < family.length; i++) {
			String[] current = family[i];
			if(current[0].equals(inputId) && current[1].equals(inputPW)) {
			// current[0]은 {"hsh", "1111"}에서의 hsh 자리를 의미
			// current[0]은 {"hsh", "1111"}에서의 1111 자리를 의미
			// && (and 연산자)를 사용해 두 값이 모두 같다면 true값이 나옴
				isLogin = true;
				// 로그인이 true가 나오게 되면
				break;
				// 반복문 종료
			}

		}
		
		if(isLogin) {
			System.out.println("Welcome Home!");
		} else {
			System.out.println("Who Are You?");
		}
		
	}

}

// 결과
// id = hhj1 / pw = 3333 - Welcome Home!
// id = hsh / pw = 2222 - Who Are You?
// id = kws / pw = 1111 - Who Are You?
