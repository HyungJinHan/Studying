// 변수로 지정하고 싶은 값에 우클릭 - Refactor - Extract Local Variable - 원하는 변수 이름 지정
// 단축키 : Alt+Shift+L	
// method로 지정하고 싶은 값에 우클릭 - Refactor - Extract Method - 원하는 method 이름 지정
// 단축키 : Alt+Shift+M
// 여기서 method 지정은 JavaScript의 function 지정과 같은 느낌

public class AccountMethodApp {
	public static double valueOfSupply; // 공급가 전역변수
	public static double varRate; // 부가가치세율 전역변수
	public static double expenseRate; // 지출비용율 전역변수
	
	public static void main(String[] args) {
		valueOfSupply = 1000000.0; // 값 지정 부분
		varRate = 0.1; // 값 지정 부분
		expenseRate = 0.3; // 값 지정 부분
		print();
	}

	private static void print() {
		System.out.println("Value of supply : "+valueOfSupply);
		// 공급가 설정
		System.out.println("VAT : "+getVAT());
		// 부가가치세 설정
		System.out.println("Total : "+getTotal());
		// 소비자가격
		System.out.println("Expense : "+getExpense());
		// 소비
		System.out.println("Income : "+getIncome());
		// 순수익
		System.out.println("Dividend (50%) : "+getDividend1());		
		System.out.println("Dividend (30%) : "+getDividend2());		
		System.out.println("Dividend (20%) : "+getDividend3());
		// 배당 5:3:2
	}

	private static double getDividend1() {
		return (getIncome())*0.5;
	}
	
	private static double getDividend2() {
		return (getIncome())*0.3;
	}
	
	private static double getDividend3() {
		return (getIncome())*0.2;
	}
	
	// 전역변수를 불러와서 return값 출력
	private static double getIncome() {
		return valueOfSupply-getExpense();
	}

	private static double getExpense() {
		return valueOfSupply*expenseRate;
	}

	private static double getTotal() {
		return valueOfSupply+getVAT();
	}

	private static double getVAT() {
		return valueOfSupply*varRate;
	}
	
}

// 결과
// Value of supply : 1000000.0
// VAT : 100000.0
// Total : 1100000.0
// Expense : 300000.0
// Income : 700000.0
// Dividend (50%) : 350000.0
// Dividend (30%) : 210000.0
// Dividend (20%) : 140000.0