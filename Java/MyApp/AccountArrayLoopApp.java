
public class AccountArrayLoopApp {

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
		
		double[] dividendRates = new double[4];
		// double 데이터타입으로 이루어진 값을 [3]개 담는 배열
		dividendRates[0] = 0.5;
		dividendRates[1] = 0.2;
		dividendRates[2] = 0.2;
		dividendRates[3] = 0.1;
		// 3개의 double 데이터를 배열에 지정
		
		int i = 0;
		while(i < dividendRates.length) {
			// 변수로 정한 i가 dividendRates의 수보다 작을 때, 반복문 종료
			System.out.println("Dividend : "+(income*dividendRates[i]));
			// income*dividendRates[i]를 통해 i값에 해당하는 배당율을 income과 곱해서 출력
			i = i + 1;
			// i의 값은 1씩 더해짐
		}
		
	}

}

// 결과
// Value of supply : 1000000.0
// VAT : 100000.0
// Total : 1100000.0
// Expense : 300000.0
// Income : 700000.0
// Dividend : 350000.0
// Dividend : 140000.0
// Dividend : 140000.0
// Dividend : 70000.0
