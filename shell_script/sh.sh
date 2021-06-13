adb="./adb.exe"
mkdir backup -p

echo "------------------------------"
echo "Welcome to Backup and Restore app!"
echo "To backup all your apps type ALL"
echo "Otherwise type the name of the apps one by one"
echo "Type FINISH when you finished with the names"
echo "Type VIEW_ALL to view all apps"
echo "------------------------------"
echo ""

all_apps=$($adb shell pm list packages -3)
cur_apps=()

while true; do
	echo -n ">> "
	read inp
	if [ $inp == "ALL" ]; then
		cur_apps=$all_apps
		break
	elif [ $inp == "FINISH" ]; then
		break
	elif [ $inp == "VIEW_ALL" ]; then
		echo "${all_apps[@]}"
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
	$adb backup -f backup/$name.ab $name
done

#adb backup -all -nosystem -f backup/$name.ab
read first_
