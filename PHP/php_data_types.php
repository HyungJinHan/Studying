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

      echo "---------Variable (변수)---------", "<br>\n", "<br>\n";
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

      echo "---------Comparison Operators (비교 연산자) &amp; Boolean Data Type (비교 연산자)---------", "<br>\n", "<br>\n";
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
      echo "3<br>";
    ?>
  </body>
</html>
