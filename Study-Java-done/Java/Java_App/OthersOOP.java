import java.io.FileWriter;
// FileWriter은 java.lang에 속하지 않기 때문에 java.io를 불러오기
import java.io.IOException;
// java.io를 불러오는 동안 없는 파일에 대한 오류 제외 불러오기

public class OthersOOP {

	public static void main(String[] args) throws IOException {
		
		// class : System, Math, FileWriter - 변수, Method를 담는 그릇 개념
		// instance : new FileWriter (f_ex1, f_ex2) - class의 복제본
		
		System.out.println(Math.PI); // 3.141592653589793 (원주율)
		System.out.println(Math.floor(Math.PI)); // 3.0 (내림)
		System.out.println(Math.round(Math.PI)); // 3 (반올림)
		System.out.println(Math.ceil(Math.PI)); // 4.0 (올림)
		
		FileWriter f_ex1 = new FileWriter("Example.txt");
		// FilWriter라는 class를 f_ex1이라는 이름으로 복제
		// txt 파일 생성 및 아래의 내용 입력
		f_ex1.write("Hello");
		f_ex1.write(" World!");
		f_ex1.write(" Im' HHJ!");
		f_ex1.close();
		// 내용 입력 후 작업 끝내기
		
		FileWriter f_ex2 = new FileWriter("Example2.txt");
		f_ex2.write("Hello");
		f_ex2.write(" World!");
		f_ex2.write(" Im' Copied HHJ!");
		f_ex2.close();

	}

}
