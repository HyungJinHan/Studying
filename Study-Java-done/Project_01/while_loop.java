import java.util.Scanner;

public class while_loop {

	public static void main(String[] args) {
		
		int i = 1;
		while(i <= 10) {
			System.out.println("This is Loop_while "+"("+i+")");
			i++;
		}
		// 결과 : This is Loop_while (1) ~ This is Loop_while (10)
		
		Scanner scan = new Scanner(System.in);
		
		int i1 = 0;
		while(i1 <= 50) {
			System.out.print("정수 입력 >> ");
			i1 = scan.nextInt();
		}
		System.out.println("반복문을 종료합니다.");
		// 결과 : 50을 넘기는 정수를 입력할 경우 반복문 종료
	}

}
