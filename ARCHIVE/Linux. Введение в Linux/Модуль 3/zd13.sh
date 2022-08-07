while true;do
read a1 op a2
if [ $a1 == "exit" ];then echo "bye";exit;fi
case $op in
 "+"|"-"|"/"|"%"|"*"|"**")
 echo $(($a1${op}$a2))
 ;;
 *)
 echo "error";exit
 ;;
esac
done