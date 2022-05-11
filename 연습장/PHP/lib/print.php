<?php
  // 제목 함수 지정
  function print_title() {
    if(isset($_GET["id"])) {
       // isset을 통해서 id값이 true인지 false인지 확인 후 id가 없는 false일 경우
       // esle 값을 도출, id가 있는 true의 경우 if에 해당하는 값을 도출
      echo htmlspecialchars ($_GET["id"]); // URL의 id에 해당하는 값을 부제목으로 가져오기
      // htmlspecialchars : php에서 sanitize하는 코드
    }
    else {
      echo "Welcome!";
    }
  }

 // 본문 함수 지정
  function print_list() {
    $list = scandir("./Data", 1);
    // list라는 변수에 폴더 스캔 담기 (뒤의 숫자는 오름차, 내림차)
    $i = 0; // i라는 변수를 0으로 지정
    while($i < count($list)) {
      $san_list = htmlspecialchars ($list[$i]);
      // $list[$i]를 sanitize 시킨 것을 san_list라는 변수로 지정
      if($list[$i] != ".") {
        if($list[$i] != "..") {
          // 불필요한 . .. 링크는 !=로 같지 않다는 조건을 걸어서 목록에 뜨지 않게 하기
          echo "<li><a href=\"index.php?id=$san_list\">$san_list</a></li>\n";
          // 태그가 깨질 수 있기 때문에 하이퍼링크 태그에 들어가는 "은 앞에
          // \(역슬래시)를 입력해서 깨지지 않게 하기 (\" xxx \")
          // htmlspecialchars ($list[$i]);를 위에서 변수로 지정한 $san_list로 입력
        }
      }
      $i = $i + 1;
    }
    // i가 count를 통해 파일의 수를 알아내고 최종적으로 i가 알아낸
    // 파일의 수보다 작으면 list 형식의 목록을 불러오다가 반복문 종료
  }

  // 목록 함수 지정
  function print_description() {
    if(isset($_GET["id"])) {
      // isset을 통해서 id값이 true인지 false인지 확인 후 id가 없는 false일 경우
      // esle 값을 도출, id가 있는 true의 경우 if에 해당하는 값을 도출
      $basename = basename($_GET["id"]);
      // basename : 경로를 제외시키고 파일명만을 선택해서 출력
      // $basename라는 변수로 지정하고 이 밑으로 $_GET["id"]을 $basename로 변경
      $file_get = strip_tags (file_get_contents("Data/".$basename), "<p><img><a><strong><u>");
      // Data 폴더와 .을 이용하여 결합 후 해당 URL의 id 값에 맞춰 내용 불러오기
      // strip_tags : 지정한 태그는 sanitize 시키지 않는다는 코드
      echo nl2br($file_get); // 함수로 지정 후 자동 줄바꿈 설정
    }
    else {
      $web_desc = "<p>The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.

                  [1] English scientist Tim Berners-Lee invented the World Wide Web in 1989.

                  He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland.

                  [2][3] The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991.
                  </p>";
      echo nl2br($web_desc);
    }
  }
?>
