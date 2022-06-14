import java.util.Scanner;

public class elseif_edu {

	public static void main(String[] args) {

		System.out.print("학점을 입력하시오. >> ");
		Scanner scan = new Scanner(System.in);
		int score = scan.nextInt();

		if(score >= 95) {
			System.out.println("입력 학점 : "+score+"점");
			System.out.println("A+학점입니다.");
		} else if (score >= 90) {
			System.out.println("입력 학점 : "+score+"점");
			System.out.println("A학점입니다.");
		} else if (score >= 85) {
			System.out.println("입력 학점 : "+score+"점");
			System.out.println("B+학점입니다.");
		} else if (score >= 75) {
			System.out.println("입력 학점 : "+score+"점");
			System.out.println("B학점입니다.");
		} else if (score >= 65) {
			System.out.println("입력 학점 : "+score+"점");
			System.out.println("C+학점입니다.");
		} else if (score >= 50) {
			System.out.println("입력 학점 : "+score+"점");
			System.out.println("C학점입니다.");
		} else if (score >= 40) {
			System.out.println("입력 학점 : "+score+"점");
			System.out.println("D+학점입니다.");
		} else if (score >= 20) {
			System.out.println("입력 학점 : "+score+"점");
			System.out.println("D학점입니다.");
		} else if (score >= 0) {
			System.out.println("입력 학점 : "+score+"점");
			System.out.println("F학점입니다.");
		}

		// 결과
		// 95~ : A+ / 90~94 : A / 85~89 : B+ / 75~84이상 : B
		// 65~74 : C+ / 50~64 : C / 40~49 : D+ / 20~39 : D
		// ~19 : F

	}

}
