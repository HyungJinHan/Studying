
public class AuthUP {

	public static void main(String[] args) {
		
		String id = "hhj"; // id 입력값이 같은지 비교를 위함
		String pw1 = "1111"; // pw 입력값이 같은지 비교를 위함
		String pw2 = "2222"; // pw 입력값이 같은지 비교를 위함
		
		String inputID = args[0];
		String inputPW = args[1];
		
		System.out.println("Hello. ");
		
		boolean isRightPW = (inputPW.equals(pw1) || inputPW.equals(pw2));
		// or 연산자를 통해 여러개의 pw들 중 맞는 경우 true 값 출력 (||)
		// boolean 형식의 변수 isRightPW 지정
		
		if(inputID.equals(id) && isRightPW) {
		// == 사용 시, 맞는 값을 입력하더라도 else로 넘어가게 됨 (false 처리)
		// ID와 PW의 일치를 동시에 표현하는 if문 (&&) / boolean 형식의 isRightPW 변수 입력
			System.out.println("Master!");
		} else {
			System.out.println("Who are you?");
		}

	}

}

//결과
//id = hhj / pw = 1111 - Hello. Master!
//id = hhj / pw = 3333 - Hello. Who are you?
