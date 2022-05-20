
public class AccountArrayApp {

	public static void main(String[] args) {
		
		// 변수로 지정하고 싶은 값에 우클릭 - Refactor - Extract Local Variable - 원하는 변수 이름 지정
		// 단축키 : Alt+Shift+L	
		double valueOfSupply = Double.parseDouble(args[0]); // 공급가 변수
		// 문자열을 실수로 변환, Run Configuration을 통해 값을 지정
		double varRate = 0.1; // 부가가치세율 변수
		double expenseRate = 0.3; // 지출비용율 변수
		
		double vat = valueOfSupply*varRate; // VAT 가격계산 변수
		double total = valueOfSupply+vat; // Total 가격계산 변수
		double expense = valueOfSupply*expenseRate; // Expense 가격계산 변수
		double income = valueOfSupply-expense; // Income 가격계산 변수
		
		double[] dividendRates = new double[3];
		// double 데이터타입으로 이루어진 값을 [3]개 담는 배열
		dividendRates[0] = 0.5;
		dividendRates[1] = 0.3;
		dividendRates[2] = 0.2;
		// 3개의 double 데이터를 배열에 지정
		
		double dividend1 = (income)*dividendRates[0];
		double dividend2 = (income)*dividendRates[1];
		double dividend3 = (income)*dividendRates[2];
		
		System.out.println("Value of supply : "+valueOfSupply);
		// 공급가 설정
		System.out.println("VAT : "+vat);
		// 부가가치세 설정	
		System.out.println("Total : "+total);
		// 소비자가격
		System.out.println("Expense : "+expense);
		// 소비
		System.out.println("Income : "+income);
		// 순수
		System.out.println("Dividend (50%) : "+dividend1);		
		System.out.println("Dividend (30%) : "+dividend2);		
		System.out.println("Dividend (20%) : "+dividend3);
		// 배당 5:3:2
		
	}

}
