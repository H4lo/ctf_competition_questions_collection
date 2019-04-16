<?php
error_reporting(0);
$flag = '********';
if (isset($_POST['name']) and isset($_POST['password'])){
	if ($_POST['name'] == $_POST['password'])
		print 'name and password must be diffirent';
	else if (sha1($_POST['name']) === sha1($_POST['password']))
		die($flag);
	else print 'invalid password';
}
?>
 
