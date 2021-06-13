adb='./adb.exe'
mkdir -p backup

for APP in $($adb shell pm list packages )
do
  name=$(echo ${APP} | sed "s/^package://")
  name2=$($adb shell pm path $name | sed "s/^package://")
  
  echo $name
  echo $name2
  $adb pull $name2 "backup/$name.apk"
done

read first_