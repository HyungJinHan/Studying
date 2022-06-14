<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    Welcome To <?php echo $_GET["where"]; ?>'s Party <?php echo $_GET["who"]; ?>!
    <!-- php URL 뒤에 ?who=xxx을 입력 후 위의 php 형식의 약속된 형식을 입력  시,
    ?name=xxx의 입력 값에 따라 도출되는 결과가 달라짐 -->
    <!-- 동시에 두개의 값을 입력하려면 ?who=조희성&where=건영아파트의 형식으로 사용 -->
  </body>
</html>
