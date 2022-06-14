import java.util.Scanner;

public class Test_txt {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		System.out.print("정수 입력 >> ");
		int A = scan.nextInt();
		System.out.println(A % 2 == 0? "짝수입니다." : "홀수입니다.");
		
		System.out.print("정수 입력 >> ");
		int B = scan.nextInt();
		System.out.println(B % 2 == 0? "짝수입니다." : "홀수입니다.");

	}

}
