<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.php">WEB</a></h1>
    <ol>
      <li><a href="index.php?id=HTML">HTML</a></li>
      <li><a href="index.php?id=CSS">CSS</a></li>
      <li><a href="index.php?id=JavaScript">JavaScript</a></li>
    </ol>
  <h2>
    <?php
      if(isset($_GET["id"])) {
         // isset을 통해서 id값이 true인지 false인지 확인 후 id가 없는 false일 경우
         // esle 값을 도출, id가 있는 true의 경우 if에 해당하는 값을 도출
        echo $_GET["id"]; // URL의 id에 해당하는 값을 부제목으로 가져오기
      }
      else {
        echo "Welcome!";
      }
    ?>
  </h2>
    <?php
      if(isset($_GET["id"])) {
        // isset을 통해서 id값이 true인지 false인지 확인 후 id가 없는 false일 경우
        // esle 값을 도출, id가 있는 true의 경우 if에 해당하는 값을 도출
        $file_get = file_get_contents("Data/".$_GET["id"]);
        // Data 폴더와 .을 이용하여 결합 후 해당 URL의 id 값에 맞춰 내용 불러오기
        echo nl2br($file_get); // 함수로 지정 후 자동 줄바꿈 설정
      }
      else {
        $file_web = file_get_contents("Data/WEB");
        echo nl2br($file_web);
      }
    ?>
</body>
</html>
