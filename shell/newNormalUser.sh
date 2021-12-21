#!/bin/bash

username="wuxuesong"
password="12345678"

# 创建新用户，并将其添加道 normalUser 的组
sudo useradd -s /bin/bash -g normalUser -G docker -m -d /home/${username} ${username}
if [ $? -eq 0 ];then
	echo "${username} is created successfully."
else
	echo "${username} is failed to be created."
	exit 1
fi

# 设置初始密码
echo -e "${password}\n${password}" | sudo passwd "$username"
if [ $? -eq 0 ];then
	echo "${username}'s password is set successfully."
else
	echo "${username}'s password is failed to be set."
fi





# 修改用户目录权限
sudo chmod 777 /home/${username}

./miniconda.sh -b -p /home/${username}/anaconda3
cd /home/${username}/anaconda3/bin
su - ${username} -c "cd /home/${username}/anaconda3/bin && ./conda init"
sudo chmod 700 /home/${username}



