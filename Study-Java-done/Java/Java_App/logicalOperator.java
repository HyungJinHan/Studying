
public class logicalOperator {

	public static void main(String[] args) {
		
		// && (그리고) : and 연산자, 둘 다 true일 경우 true, 하나라도 false의 경우 false
		System.out.println(true && true); // true
		System.out.println(false && true); // false
		System.out.println(true && false); // false
		System.out.println(false && false); // false
		
		// 줄바꿈
		System.out.println(System.lineSeparator());
		
		// || (또는) : or 연산자, 둘 중에 하나라도 true일 경우 true
		System.out.println(true || true); // true
		System.out.println(false || true); // true
		System.out.println(true || false); // true
		System.out.println(false || false); // false
		
		// 줄바꿈
		System.out.println(System.lineSeparator());
		
		// ! (부정) : not 연산자, 입력값의 반대의 결과 출력
		System.out.println(!true); // false
		System.out.println(!false); // true

	}

}
