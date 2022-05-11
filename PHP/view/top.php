<?php
  require_once("lib/print.php");
  // top.php에 존재하는 print_xxx()가 어디에서 왔는지 알려주는 역할
  // index에서 print.php, top.php를 요청함 → print.php, top.php 실행됨
  // top.php와 print.php에서 require("lib/print.php");가 겹치면서 중복 실행
  // 결국 오류가 나기 때문에 require_once라는 코드를 사용해야함
?>
<!doctype html>
<html>
<head>
  <title>
    <?php
      print_title(); // 위에서 지정한 제목 함수 출력
    ?>
  </title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.php">WEB</a></h1>
    <ul>
      <?php
        print_list(); // 위에서 지정한 본문 함수 출력
      ?>
    </ul>
