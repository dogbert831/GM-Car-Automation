/*
Copyright 2016 jryanishere

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

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
