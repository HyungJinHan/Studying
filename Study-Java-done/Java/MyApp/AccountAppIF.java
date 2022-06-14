
public class AccountAppIF {

	public static void main(String[] args) {
		
		// 변수로 지정하고 싶은 값에 우클릭 - Refactor - Extract Local Variable - 원하는 변수 이름 지정
		// 단축키 : Alt+Shift+L	
		double valueOfSupply = Double.parseDouble(args[0]); // 공급가 변수 (1000000.0 or 9000.0)
		// 문자열을 실수로 변환, Run Configuration을 통해 값을 지정
		double varRate = 0.1; // 부가가치세율 변수
		double expenseRate = 0.3; // 지출비용율 변수
		
		double vat = valueOfSupply*varRate; // VAT 가격계산 변수
		double total = valueOfSupply+vat; // Total 가격계산 변수
		double expense = valueOfSupply*expenseRate; // Expense 가격계산 변수
		double income = valueOfSupply-expense; // Income 가격계산 변수
		
		double dividend1;
		double dividend2;
		double dividend3;
		
		if(income > 10000.0) {
			dividend1 = (income)*0.5; // Dividend 5할 계산 변수
			dividend2 = (income)*0.3; // Dividend 3할 계산 변수
			dividend3 = (income)*0.2; // Dividend 2할 계산 변수
		} else {
			dividend1 = (income)*1; // Dividend 5할 계산 변수
			dividend2 = (income)*0; // Dividend 3할 계산 변수
			dividend3 = (income)*0; // Dividend 2할 계산 변수
		}
		// if를 사용하여 income이라는 변수의 값이 10000.0보다 크다면 5:3:2 배분
		// else를 사용하여 그렇지 않다면 10:0:0 배분
		
		System.out.println("Value of supply : "+valueOfSupply);
		// 공급가 설정
		System.out.println("VAT : "+vat);
		// 부가가치세 설정	
		System.out.println("Total : "+total);
		// 소비자가격
		System.out.println("Expense : "+expense);
		// 소비
		System.out.println("Income : "+income);
		// 순수익
		System.out.println("Dividend 1 : "+dividend1);		
		System.out.println("Dividend 2 : "+dividend2);		
		System.out.println("Dividend 3 : "+dividend3);
		// 배당 5:3:2
		
	}

}

// 결과 (income > 10000.0)
// Value of supply : 1000000.0
// VAT : 100000.0
// Total : 1100000.0
// Expense : 300000.0
// Income : 700000.0
// Dividend 1 : 350000.0
// Dividend 2 : 210000.0
// Dividend 3 : 140000.0

// 결과 (income < 10000.0)
// VAT : 900.0
// Total : 9900.0
// Expense : 2700.0
// Income : 6300.0
// Dividend 1 : 6300.0
// Dividend 2 : 0.0
// Dividend 3 : 0.0
