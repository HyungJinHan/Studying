// 변수로 지정하고 싶은 값에 우클릭 - Refactor - Extract Local Variable - 원하는 변수 이름 지정
// 단축키 : Alt+Shift+L	
// method로 지정하고 싶은 값에 우클릭 - Refactor - Extract Method - 원하는 method 이름 지정
// 단축키 : Alt+Shift+M
// 여기서 method 지정은 JavaScript의 function 지정과 같은 느낌
// class 지정이라는 것은 소속을 바꾸는 것이라고 생각 (객체지향 프로그래밍)
// instance는 class 전체를 복제해서 변수화한다고 생각 (해당 class의 static을 지워야 함)

class Account {
	public double valueOfSupply; // 공급가 전역변수
	public double varRate; // 부가가치세율 전역변수
	public double expenseRate; // 지출비용율 전역변수
	
	public void print() {
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

	public double getDividend1() {
		return (getIncome())*0.5;
	}
	
	public double getDividend2() {
		return (getIncome())*0.3;
	}
	
	public double getDividend3() {
		return (getIncome())*0.2;
	}
	
	// 전역변수를 불러와서 return값 출력
	public double getIncome() {
		return valueOfSupply-getExpense();
	}

	public double getExpense() {
		return valueOfSupply*expenseRate;
	}

	public double getTotal() {
		return valueOfSupply+getVAT();
	}

	public double getVAT() {
		return valueOfSupply*varRate;
	}
	
}

public class AccountClassApp {
	
	public static void main(String[] args) {
		Account a1 = new Account();
		// class를 복제하는 instance 작업 (class 자체를 하니의 변수화하는 느낌)
		a1.valueOfSupply = 1000000.0;
		a1.varRate = 0.1;
		a1.expenseRate = 0.3;
		a1.print();
		
		System.out.println(System.lineSeparator());
		// 줄바꿈
		
		Account a2 = new Account();
		a2.valueOfSupply = 1000000.0;
		a2.varRate = 0.2;
		a2.expenseRate = 0.4;
		a2.print();
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


// Value of supply : 1000000.0
// VAT : 200000.0
// Total : 1200000.0
// Expense : 400000.0
// Income : 600000.0
// Dividend (50%) : 300000.0
// Dividend (30%) : 180000.0
// Dividend (20%) : 120000.0