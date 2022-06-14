<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP Data Types</title>
  </head>
  <body>
    <?php
      echo "---------Number (숫자 : Integers) & Operator---------", "<br>\n";
      echo "<br>"; // 브라우저 상의 줄바꿈 (소스코드는 줄바꿈 안됨)
      echo 1;
      echo "\n"; // 소스코드 상의 줄바꿈 (브라우저는 줄바꿈 안됨)
      echo -1.3;
      echo "<br>\n"; // 브라우저, 소스코드 동시에 줄바꿈
      echo 1+1, "<br>\n";
      echo 15*3, "<br>\n";
      echo 9/3, "<br>\n";
      echo 8-19, "<br>\n";
      echo 2-5*3, "<br>\n", "<br>\n";

      echo "---------String & String Operator (문자열 & 문자 연산자)---------", "<br>\n", "<br>\n";
      echo "Hello World", "<br>\n";
      echo "Hello \"W\"orld", "<br>\n", "<br>\n"; // \를 붙이면 태그로써의 역할 상실

      echo "---------★ Concatenation Operator (결합 연산자) ★---------", "<br>\n", "<br>\n";
      echo "Hello"." World", "<br>\n"; // .을 써서 좌우를 결합해서 하나의 문자열로 표현
      echo "Hello,"." World!", "<br>\n","<br>\n";

      echo "---------String Length (문자열 길이)---------", "<br>\n", "<br>\n";
      $str = "Hello World"; // PHP 변수 문법
      echo strlen($str), "<br>\n"; // 함수 버전
      echo strlen("Hello, World!"), "<br>\n", "<br>\n"; // 일반 버전

      echo "---------Variable (변수 $)---------", "<br>\n", "<br>\n";
      $a = 10; $b = 22;
      echo $a + $b, "<br>\n";
      $name1 = "한상현"; // 문자를 결합하기 위해 변수 앞뒤에 .이라는 결합 연산자 입력
      $name2 = "조희성";
      echo "Lorem ipsum dolor sit amet, ".$name1." consectetur adipisicing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, ".$name1." quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
        in voluptate velit esse ".$name2." cillum dolore eu fugiat nulla pariatur.
        Excepteur sint ".$name1." occaecat cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est ".$name2." laborum.", "<br>\n", "<br>\n";

      echo "---------Function (함수)---------", "<br>\n", "<br>\n";
      $htr = "Lorem ipsum dolor sit amet, consectetur adipisicing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
        in reprehenderit in voluptate velit esse cillum dolore
        eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.";
      echo nl2br($htr), "<br>\n", "<br>\n", strlen($htr), "<br>\n", "<br>\n";
      // echo nl2br($xxx) : 엔터친 부분 자동 줄바꿈

      function basic() { // 함수의 이름이 basic
        print("hahahahahahaha <br>\n"); // 함수 호출 문법
        print("hehehehehehehe <br>\n <br>\n");
      }
      basic();

      function sum($left, $right) { // 좌우를 변수(parameter)로 지정
        print($left + $right); // 좌우 변수를 더해서 출력하도록 지정
        print("<br>\n"); // 함수 내에 줄바꿈 추가
      }
      sum(2, 4); // () 내부의 값(argument)에 따라 도출되는 결과가 다름
      sum(10, 100);

      echo "<br>\n", "<br>\n", "---------Return (출력)---------", "<br>\n", "<br>\n";
      function sum2($left, $right) { // 변수를 좌우로 지정하고
        return $left + $right; // 지정한 변수를 더해서 출력(return)하도록 지정
        // return 다음으로 오는 함수는 무시됨 (return은 함수를 종료시킴)
      }
      print(sum2(4, 10));
      print("<br>\n");
      print(sum2(10, 87));
      file_put_contents("result.txt", sum2(4, 10)); // print된 결과를 txt 파일에 저장

      echo "<br>\n", "<br>\n", "---------Comparison Operators (비교 연산자) &amp; Boolean Data Type (비교 연산자)---------", "<br>\n", "<br>\n";
      echo ("1123"." → "); var_dump("1123"); echo("<br>\n");
      echo ("1123+5"." → "); var_dump(1123+5); echo("<br>\n");
      echo ("1==3"." → "); var_dump(1==3); echo("<br>\n");
      echo ("1<3"." → "); var_dump(1<3); echo("<br>\n");
      echo ("10>=10"." → "); var_dump(10>=10); echo("<br>\n"), "<br>\n";
      //var_dump = data type이 무엇인지 알려주며 출력

      echo "---------Conditional Statements (조건문 if, else)---------", "<br>\n", "<br>\n";
      echo "1<br>";
      if(true) {
        echo "2-1<br>";
      }
      else {
        echo "2-2<br>";
      }
        echo "3<br>", "<br>\n";

      echo "---------Loop (반복문 while)---------", "<br>\n", "<br>\n";
      echo "1<br>";
      $i = 0; // i라는 변수에 0이라는 값으로 지정
      while ($i < 5) { // i의 값이 원하는 수에 도달하면 반복이 멈추게끔 지정
        echo "2";
        $i = $i + 1; // while이 실행 될 때마다 i에 1씩 더해진다
      }
      echo "<br>\n";
      $t = 0;
      while ($t <= 4) {
        echo "3";
        $t = $t + 1;
      }

      echo "<br>\n", "<br>\n", "---------Array (배열)---------", "<br>\n", "<br>\n";
      $family = array("hsh", "jhs", "hhj1", "hhj2");
      // family라는 변수에 hsh, jhs, hhj1, hhj2 담기
      echo $family[2], "<br>\n"; // family내의 원하는 값을 도출
      echo $family[1], "<br>\n";
      echo count($family), "<br>\n"; // family라는 변수 내의 구성 요소의 수
      array_push($family, "kws", "jhk", "kjh1", "kjh2"); // family라는 변수 내에 구성 요소를 끝에 추가
      var_dump($family);

      echo "<br>\n", "<br>\n", "---------Array Combine (배열 합치기)---------", "<br>\n", "<br>\n";
      $hanfamily = array("hsh", "jhs", "hhj1", "hhj2");
      $rules = array("father", "mother", "big son", "small son");
      $home = array_combine($hanfamily, $rules);
      var_dump($home);
    ?>
  </body>
</html>
