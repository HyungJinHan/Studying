import java.util.Scanner;

public class if_edu {

	public static void main(String[] args) {
		
		System.out.print("나이를 입력하시오. >> ");
		// 나이 입력의 원활함을 위한 텍스트 출력
		Scanner scan = new Scanner(System.in);
		// input도구(scanner) 생성
		int age = scan.nextInt();
		// scan이라는 input도구(scanner)를 age라는 변수에 지정
		
		if(age >= 20) {
			System.out.println("성인 인증에 성공했습니다.");
			// age >= 20가 true일 경우
		} else {
			System.out.println("성인 인증에 실패했습니다.");
			// age >= 20가 false일 경우
		}
	}

}
