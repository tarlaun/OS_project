adb="adb"

all_apps=$(ls backup)
cur_apps=()
all_flag=0


cur_apps=()
all_flag=0

selected=$(python restore_gui.py $all_apps)

if [ $selected == "ALL" ]; then
    for APP in ${app_list[@]}; do
        cur_apps+=($(echo ${APP} | sed 's/\r//g'))
    done
    all_flag=1
else
    for APP in $selected; do
        cur_apps+=($(echo ${APP} | sed 's/\r//g'))
    done
fi

echo "Now the restoring process begins: "

for APP in "${cur_apps[@]}"; do
	if test -f "backup/$APP/$APP.apk"; then
		$adb install backup/$APP/$APP.apk
		if [ $all_flag == 0 ]; then
			if test -f "backup/$APP/$APP.ab"; then
				$adb restore backup/$APP/$APP.ab
			fi
		fi
	fi
done

if [ $all_flag == 1 ]; then
	mkdir "backup/alldata" -p
	$adb restore -all -nosystem -f backup/alldata/alldata.ab
fi

echo "Restoration complete!"
read first_