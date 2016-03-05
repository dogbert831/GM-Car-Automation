<?php
$arg = $_GET['command'];
switch ($arg){ 
	case "start":
		exec("sudo python cgi-script/keyfob.py start");
		echo "Your car has been started.";
		break;
        case "stop":
                exec("sudo python cgi-script/keyfob.py stop");
                echo "Your car has been stopped.";
                break;
        case "lock":
                exec("sudo python cgi-script/keyfob.py lock");
                echo "Your car has been locked.";
                break;
        case "unlock":
                exec("sudo python cgi-script/keyfob.py unlock");
                echo "Your driver's door has been unlocked.";
                break;
        case "unlock_all":
                exec("sudo python cgi-script/keyfob.py unlock_all");
                echo "Your car has been unlocked.";
                break;
        case "panic":
                exec("sudo python cgi-script/keyfob.py panic");
                echo "The panic command has been sent to your car.";
                break;
        case "trunk":
                exec("sudo python cgi-script/keyfob.py trunk");
                echo "Your car's trunk has been triggered.";
                break;
}
?>
