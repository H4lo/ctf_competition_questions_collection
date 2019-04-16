

<!DOCTYPE html>
<html>
<head>
   <title>Dota WebSite</title>
   <link href="css/bootstrap.min.css" rel="stylesheet">
   <script src="js/jquery.min.js"></script>
   <script src="js/bootstrap.min.js"></script>
</head>
<body>

<nav class="navbar navbar-default" role="navigation">
   <div class="navbar-header">
      <a class="navbar-brand" href="#">Dota WebSite</a>
   </div>
   <div>
      <ul class="nav navbar-nav">
         <li class="active"><a href="index.php">Index</a></li>
         <li><a href="index.php?act=news">News</a></li>
         <li><a href="index.php?act=photos&pid=1">Photos</a></li>
         <li><a href="flag.php">Flag</a></li>
         </li>
      </ul>
   </div>
</nav>
<div class="span7 text-center">
<?php
   $act = '';
   if(!isset($_GET['act'])){
      print "<h1>Welcome To Dota WebSite!</h1>";
   }else{
      $act = $_GET['act'];
      switch ($act) {
         case 'news':
            if(isset($_GET['nid'])){

               if(preg_match("/[a-zA-Z]/",$_GET['nid'])){
                  exit("Illegal operation!");
               }elseif(strlen($_GET[nid])>5){
                  exit("Illegal operation!");
               }else{
                  echo "<p class=lead>";
                  system("head ./news/" . $_GET['nid']);
                  echo "</p>";
               }

            }else{
               echo "<h3><a href=index.php?act=news&nid=1>鱼人守卫</a></h3>";
               echo "<h3><a href=index.php?act=news&nid=2>黑暗游侠</a></h3>";
               echo "<h3><a href=index.php?act=news&nid=3>血魔</a></h3>";

            }
            break;

         case 'photos':
            if(isset($_GET['pid'])){
               $_GET['pid'] = intval($_GET['pid']);
?>
      
                  <div class="col-sm-6 col-md-3">
                     <div class="thumbnail">
                        <img src="/images/<?php echo $_GET['pid'];?>.jpg" alt="">
                     </div>
                  </div>

<?php
            }
            break;


         default:
            header("location:index.php");
            break;
      }
   }
?>
</div>
</body>
</html>

