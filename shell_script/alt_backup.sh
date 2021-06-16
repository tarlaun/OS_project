adb="adb"
mkdir backup -p


all_apps=$($adb shell pm list packages -3)
cur_apps=()
all_flag=0
app_list=()
for APP in $all_apps; do
    name=($(echo ${APP} | sed "s/^package://" | sed 's/\r//g'))
    app_list+=($name)
done
selected=$(python alt_backup_gui.py ${app_list[@]})

if [ $selected == "ALL" ]; then
    for APP in ${app_list[@]}; do
        cur_apps+=($APP)
    done
    all_flag=1
else
    for APP in $selected; do
        cur_apps+=($APP)
    done
fi

echo "Now the backup process begins: "

for name in "${cur_apps[@]}"; do
	name2=$($adb shell pm path $name | sed "s/^package://")
	echo $name
	mkdir "backup/$name" -p
	for pth in $name2; do
		$adb pull /$pth "backup/$name/$name.apk"
		#echo $(aapt2 dump badging "backup/$name/$name.apk" | sed -n "s/^application-label:'\(.*\)'/\1/p")
		#TODO get app names before showing
	done
	if [ $all_flag == 0 ]; then
		$adb backup -f backup/$name/$name.ab $name
		#TODO automatic accept
	fi
done
if [ $all_flag == 1 ]; then
	mkdir "backup/alldata" -p
	$adb backup -all -nosystem -f backup/alldata/alldata.ab
fi
echo "Backup completed!"
read first_