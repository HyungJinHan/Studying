
public class String_ex {

	public static void main(String[] args) {
		
		// String VS Character
		System.out.println("Hello HHJ!"); // String (문자열)
		System.out.println('H'); // Character (문자) : ''는 하나의 글자일 경우
		
		// New Line
		System.out.println("Hello "
				+ "HHJ!"); // Ctrl+Enter로 자동 줄바꿈 (코드상에서만)
		
		System.out.println("Hello \nHHJ!"); // \n은 화면상의 줄바꿈
		System.out.println("Hello \"HHJ!\""); // \"의 경우 문자로써의 화면에 출력
		
		// String Operation
		System.out.println("Hello HHJ!".length()); // 10 : 문자열의 글자 수
		System.out.println("Hello HHJ!".replace("HHJ", "HSH"));
		System.out.println("Hello [[name]]".replace("[[name]]", "HHJ"));
		
	}

}
