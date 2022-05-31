
public class Operator {

	public static void main(String[] args) {
		
		// === 산술연산자 ===
		int num_1 = 100;
		int num_2 = 10;
		System.out.println(num_1 + num_2); // 결과 : 110
		System.out.println(num_1 - num_2); // 결과 : 90
		System.out.println(num_1 * num_2); // 결과 : 1000
		System.out.println(num_1 / num_2); // 결과 : 10
		System.out.println(num_2 % num_1); // 결과 : 10
		System.out.println("num_1 + num_2 = " + num_1 + num_2); // 결과 : num_1 + num_2 = 10010
		// 문자열 + 숫자 = 문자열로 출력
		int num_3 = 50;
		num_3 = num_3 + 30;
		System.out.println(num_3); // 결과 : 80
		
		// === 증감연산자 (++) ===
		int i = 30;
		System.out.println(++i); // 결과 : 31 (앞의 증감연산자는 출력과 동시에 1을 더함)
		System.out.println(i++); // 결과 : 31 (뒤의 증감연산자는 출력한 후의 값에 1을 더함)
		System.out.println(i); // 결과 : 32 (결과적으로 i++로 인해 i값에 1이 더해짐)
		// ++ : 증감연산자로 1씩 증가를 의미
		
		// === 논리연산자 (Boolean) ===
		int a = 1;
		int b = 2;
		System.out.println(a == b); // 결과 : false
		System.out.println(a != b); // 결과 : true
		System.out.println(a > b); // 결과 : false
		System.out.println(a >= b); // 결과 : false
		System.out.println(a < b); // 결과 : true
		System.out.println(a <= b); // 결과 : true
		System.out.println(true && true);// 결과 : true (&& : and 연산자로 둘 다 참이어야 true)
		System.out.println(true && false);// 결과 : false
		System.out.println(true || true);// 결과 : true (|| : or 연산자로 둘 중 하나만 참이어도 true)
		System.out.println(true || false);// 결과 : true
		
		// === 삼항연산자 ===
		int A = 1;
		int B = 2;
		System.out.println(A == B? "True" : "False"); // 결과 : False
		System.out.println(A != B? "True" : "False"); // 결과 : True
		// 조건문(if)과 비슷하며 A와 B가 같다면 True를, 다르다면 False를 출력

	}

}
