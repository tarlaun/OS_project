mkdir backup -p


for APP in $(adb shell pm list packages -3)
do
  name=$(echo ${APP} | sed "s/^package://")
  name2=$(adb shell pm path $name | sed "s/^package://")
  for pth in $name2
  do
    adb pull $pth "backup/$name.apk"
  done
#  adb backup -f backup/$name.ab $name
done
adb backup -all -nosystem -f backup/$name.ab
read first_
