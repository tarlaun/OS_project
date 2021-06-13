adb="./adb.exe"
mkdir backup -p

echo "------------------------------"
echo "Welcome to Backup and Restore app!"
echo "To backup all your apps type ALL"
echo "To choose from a list of your files, type CONF"
echo "Otherwise type the name of the apps one by one"
echo "Type FINISH when you finished with the names"
echo "Type VIEW_ALL to view all apps"
echo "------------------------------"
echo ""

all_apps=$($adb shell pm list packages -3)
cur_apps=()
all_flag=0


while true; do
	echo -n ">> "
	read inp
	if [ $inp == "ALL" ]; then
		cur_apps=$all_apps
		all_flag=1
		break
	elif [ $inp == "FINISH" ]; then
		break
	elif [ $inp == "VIEW_ALL" ]; then
		echo "${all_apps[@]}"
	elif [ $inp == "CONF" ]; then
		for APP in $all_apps; do
			while true; do
				echo "do you want to include $APP? (y/n)"
				echo -n ">> "
				read inp
				if [ $inp == "y" ]; then
					cur_apps += ($(echo ${APP} | sed 's/\r//g'))
					break
				elif [ $inp == "n"]; then
					break
				else
					echo "invalid input. please try again."
				fi
			done
		done
	else
		flg=0
		for APP in $all_apps; do
			if echo "$APP" | grep -q "$inp"; then
				if [ $flg == 0 ]; then
					echo "matched with $APP"
					cur_apps+=($(echo ${APP} | sed 's/\r//g'))
					flg=1
					#break # optional to comment
				else 
					echo "unselected candidate $APP"
				fi
			fi
		done
		
		if [ $flg == 0 ]; then
			echo "no match found"
		fi
	fi
done


for APP in "${cur_apps[@]}"; do
	echo $APP
	name=$(echo ${APP} | sed "s/^package://")
	name2=$($adb shell pm path $name | sed "s/^package://")
	for pth in $name2; do
		$adb pull /$pth "backup/$name.apk"
	done
	if [ all_flag == 0]; then
		$adb backup -f backup/$name.ab $name
	fi
done
if all_flag; then
	adb backup -all -nosystem -f backup/$name.ab
fi
read first_
