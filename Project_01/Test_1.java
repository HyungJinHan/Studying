import java.util.Scanner;

public class Test_1 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		System.out.print("숫자 입력 >> ");
		int number = scanner.nextInt();
		System.out.println(number);
		
		int num_1 = 100;
		int num_2 = 50;
		System.out.println("변수 num_1의 값은 "+num_1+" 입니다.");
		System.out.println("변수 num_2의 값은 "+num_2+" 입니다.");
		System.out.print("합계 : ");
		System.out.println(num_1 + num_2);
		System.out.print("평균 : ");
		System.out.println((num_1 + num_2)/2);
		
		System.out.print("첫번째 정수 입력 >> ");
		int num_3 = scanner.nextInt();
		
		System.out.print("두번째 정수 입력 >> ");
		int num_4 = scanner.nextInt();
		
		// System.out.println(num_3);
		// System.out.println(num_4);
		
		System.out.print("합계 : ");
		System.out.println(num_3 + num_4);
		System.out.print("평균 : ");
		System.out.println((num_3 + num_4)/2);
		
		System.out.print("정수 입력 >> ");
		int A = scanner.nextInt();
		System.out.println(A % 2 == 0? "짝수입니다." : "홀수입니다.");
		
		System.out.print("정수 입력 >> ");
		int B = scanner.nextInt();
		System.out.println(B % 2 == 0? "짝수입니다." : "홀수입니다.");
	}

}
