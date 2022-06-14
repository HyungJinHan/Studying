
public class Variable_Datatype_2 {

	public static void main(String[] args) {
		
		// 1. 논리형
		boolean name1 = 1 == 1;
		System.out.println(name1); // true
		
		// 2. 문자형
		char name2 = 'a'; // 문자가 하나 이상일 경우 문자열로 취급 (''은 문자)
		System.out.println(name2); // a
		
		String name3 = "abc"; // ""은 문자열
		System.out.println(name3); // abc
		
		// 3. 정수형
		int name4 = 8;
		System.out.println(name4); // 8
		
		// 4. 실수형
		double name5 = 3.14;
		System.out.println(name5); // 3.14
		
		float name6 = 1.5f; // float 지정을 위해 값 뒤에 f 입력
		System.out.println(name6); // 1.5
		
		// 5. 상수형
		final String name7_fin = "This is name7_fin"; // 상수
		// name7_fin = "This is name7_fin, too"; → 결과 : Error
		// name7_fin은 위에서 상수 This is name7_fin으로 지정했기 때문에 따로 변수 지정 후 내용 변경 불가
		System.out.println(name7_fin);
		// 결과 : This is name7_fin (변경 불가)
		
		String name7_var = "This is name7_var"; // 변수
		name7_var = "This is name7_var, too";
		name7_var = "This is name7_var, either";
		System.out.println(name7_var);
		// 결과 : This is name7_var, either (몇번이든 변경 가능)
		
		final String name8_fin; // 상수
		name8_fin = "This is name8_fin";
		System.out.println(name8_fin);
		// 결과 : This is name8_fin (변경 불가)
		
		String name8_var; // 변수
		name8_var = "This is name8_var";
		name8_var = "This is name8_var, too";
		System.out.println(name8_var);
		// 결과 : This is name8_var, too (몇번이든 변경 가능)
		
	}

}
