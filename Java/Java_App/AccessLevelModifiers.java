
class Greeting {
	public static void Hi() {
		System.out.println("Hi!");
	}
}

public class AccessLevelModifiers {
	public static void main(String[] args) {
		Greeting.Hi(); // Error
	}

}
