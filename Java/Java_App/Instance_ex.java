import java.io.FileNotFoundException;
// 파일이 없을 시에 예외사항으로 처리한다라는 뜻
// PrintWriter라는 Constructor를 사용할 때 나올수 있는 에러에 대한 import
import java.io.IOException;
import java.io.PrintWriter;

public class Instance_ex {

	public static void main(String[] args) throws IOException {
		
		PrintWriter p1 = new PrintWriter("result1.txt");
		// p1은 instance
		// result1.txt를 패키지에 생성
		p1.write("Hello HHJ1");
		// result1.txt에 Hello HHJ1 입력
		p1.close();
		// result1.txt 작업을 끝냄
		
		PrintWriter p2 = new PrintWriter("result2.txt");
		p2.write("Hello HHJ2");
		p2.close();
	}

}
