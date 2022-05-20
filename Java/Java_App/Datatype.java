// Java의 동작 원리
// 1. .java 라는 사람이 이해할 수 있는 소스 코드를 작성한다. (.java)
// 2. 1번의 코드를 컴파일하여 컴퓨터가 이해할 수 있게끔 바꾼다. (.class)  
// 3. 컴퓨터가 자바라는 것을 이해시키기 java virtual machine으로 보낸다.
// 4. 컴퓨터가 java virtual machine한테 받은걸 출력한다.

public class Datatype {
	
	public static void main(String[] args) {
	// 여기까지는 기본적으로 입력해야 할 코드
		System.out.println("Hello World");
		// System.out.println(in이 아닌 ln)() : 화면 출력
		System.out.println(6); // Number (숫자)
		System.out.println("six"); // String (문자열)
		System.out.println("6"); // String 6 (문자열로써의 6)
		System.out.println(6+6); // 숫자로써 계산 된 12
		System.out.println("6"+"6"); // 문자열로써 66
		System.out.println("111146554".length()); // 문자열의 길이(수)	
	}

}
