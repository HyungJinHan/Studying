import java.util.Scanner;
// Scanner 불러오기 (import)

public class input_output {

	public static void main(String[] args) {
		
		// → 이것은 주석을 의미
		
		// 1. 출력하기
		
		System.out.println("This is String");
		// 결과 : This is String
		
		String var = "This is Variable";
		System.out.println(var);
		// 결과 : This is Variable
		
		System.out.println(var + " and " + "This is String");
		// 결과 : This is Variable and This is String
		
		System.out.print("This is");
		System.out.print(" print");
		// 결과 : This is print
		
		System.out.println("This is");
		System.out.println("println");
		// 결과 : This is
		//		 println
		
		// 2. 입력하기
		
		Scanner scan = new Scanner(System.in);
		// Scanner 도구 불러오기 (import)
		
		System.out.print("Input Number >>");
		
		int num = scan.nextInt();
		// 결과 : 콘솔창에 숫자 입력 가능
		
		System.out.println(num);
		// 결과 : 콘솔창에 입력한 숫자 출력 (10000)
		
		System.out.print("InputContext Name >>");
		
		String str = scan.next();
		// 결과 : 콘솔창에 문자열 입력 가능
		
		System.out.println("My name is " + str + " Nice to meet you");
		// 결과 : 콘솔창에 입력한 문자열 출력 (My name is HHJ Nice to meet you)
		
	}

}
