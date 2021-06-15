adb="./adb.exe"

echo "------------------------------"
echo "Welcome back!"
echo "Let's restore your previously backed up apps!"
echo "To restore all backed up apps, type ALL."
echo "To choose from a list of your files, type SEL."
echo "Otherwise, type the name of the apps one by one."
echo "Type FINISH when you finished with the names."
echo "Type VIEW_ALL to view all apps."
echo "------------------------------"
echo ""

all_apps=$(ls backup)
cur_apps=()
all_flag=0

while true; do
	echo -n ">> "
	read inp
	if [ $inp == "ALL" ]; then
		for APP in $all_apps; do
		cur_apps+=($(echo ${APP} | sed 's/\r//g'))
		done
		all_flag=1
		break
	elif [ $inp == "FINISH" ]; then
		break
	elif [ $inp == "VIEW_ALL" ]; then
		echo "${all_apps[@]}"
	elif [ $inp == "SEL" ]; then
		for APP in $all_apps; do
			while true; do
				echo "Do you want to include $APP? (y/n/break)"
				echo -n ">> "
				read inp
				if [ $inp == "y" ]; then
					cur_apps+=($(echo ${APP} | sed 's/\r//g'))
					break
				elif [ $inp == "n" ]; then
					break
				elif [ $inp == "break" ]; then
					break 2
				else
					echo "Invalid input. Please try again."
				fi
			done
		done
	else
		selected_app="$(python backup_python.py $inp $all_apps)"
		if [ $selected_app == "no_match" ]; then
			echo "no match found"
		else
			echo "matched with $selected_app"
			cur_apps+=($(echo ${selected_app} | sed 's/\r//g'))
		fi	

	fi
done

echo "Now the restoring process begins: "

for APP in "${cur_apps[@]}"; do
	echo $APP
	name=$(echo ${APP} | sed "s/^package://")
	name2=$($adb shell pm path $name | sed "s/^package://")
	if test -f "backup/$APP/$APP.apk"; then
		$adb install backup/$APP/$APP.apk
		if test -f "backup/$APP/$APP.ab"; then
			$adb restore backup/$APP/$APP.ab
		fi
	fi
done

echo "Ressurection completed!"
read first_
