
public class Auth {

	public static void main(String[] args) {
		
		String id = "hhj"; // id 입력
		String pw = "1111"; // pw 입력
		
		String inputID = args[0];
		String inputPW = args[1];
		
		System.out.println("Hello. ");
		
		// if(inputID == id) { == 사용 시, 맞는 값을 입력하더라도 else로 넘어가게 됨 (false 처리)
		if(inputID.equals(id) && inputPW.equals(pw)) {
		// ID와 PW의 일치를 동시에 표현하는 if문 (&&)
			System.out.println("Master!");
		} else {
			System.out.println("Who are you?");
		}

	}

}

// 결과 (id 혹은 pw 틀릴 시)
// Hello. 
// Who are you?

// 결과 (id, pw 맞을 시)
// Hello. 
// Master!