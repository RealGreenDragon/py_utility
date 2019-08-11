# VirtualBox Ubuntu (and derivates) x64 Configuration Guide

Author: Daniele Giudice

## Install/Update VirtualBox Guest Additions + Enable Shared Folders Access

#### Update all packages + Install 'VirtualBox Guest Additions' dependencies
sudo apt -y update && sudo apt -y upgrade && sudo apt -y install build-essential virtualbox-guest-dkms linux-headers-virtual && sudo apt -y autoremove && sudo apt -y clean

#### Mount 'Guest Additions CD' from menu "Devices->Insert Guest Additions CD image..."

#### Install/Update Guest Additions
sudo "$(df --output=target | grep VBox_GAs_)/VBoxLinuxAdditions.run"

#### Unmount 'Guest Additions CD'
sudo umount -f "$(df --output=target | grep VBox_GAs_)"

#### Remove 'Guest Additions CD' by right click on disk icon in vbox windows bottom-right and select "Remove disk from virtual drive"

#### Add current user in 'vboxsf' group to grant access to shared folders
sudo usermod -aG vboxsf $(whoami)

#### Reboot to enable changes
sudo reboot

## Set Italian Keyboard

#### Valid until reboot (No GUI Environment)
sudo loadkeys it

#### Valid until reboot (GUI Environment)
sudo setxkbmap it

#### Permanent
sudo dpkg-reconfigure keyboard-configuration

## Some useful software

#### Base software
sudo apt install -y curl wget net-tools unrar ffmpeg vlc vim python python-pip git && sudo apt -y autoremove && sudo apt -y clean

#### Pyhton Modules
sudo pip install --upgrade wheel setuptools twine requests python_utils pycryptodome

#### TeX Live
sudo apt install -y texlive-latex-extra

#### Notepadqq (latest version)
sudo add-apt-repository -y ppa:notepadqq-team/notepadqq && sudo apt -y update && sudo apt install -y notepadqq

#### Atom (latest version)
wget -O ~/atom-amd64.deb https://atom.io/download/deb && sudo apt -y install ~/atom-amd64.deb && rm -f ~/atom-amd64.deb

#### XAMPP v7.3.8 x64 + Shortcut scripts
wget -O ~/xampp-x64.run "https://www.apachefriends.org/xampp-files/7.3.8/xampp-linux-x64-7.3.8-0-installer.run" && chmod a+x ~/xampp-x64.run && sudo ~/xampp-x64.run --mode unattended && rm -f ~/xampp-x64.run && sudo chmod o+rx -R /opt/lampp/htdocs/ && echo "/opt/lampp/manager-linux-x64.run" > ~/xampp_gui.sh && echo "/opt/lampp/lampp" > ~/xampp_service.sh && chmod a+x ~/xampp_*.sh

#### Docker (latest version) -> Reboot required
curl -fsSL https://get.docker.com -o ~/get-docker.sh && chmod a+x ~/get-docker.sh && sudo sh ~/get-docker.sh && rm -f ~/get-docker.sh && sudo usermod -aG docker $(whoami) && sudo reboot

#### Wireshark (latest version) -> Reboot required
sudo apt -y install wireshark && sudo usermod -aG wireshark $(whoami) && sudo reboot

#### Kathara + GUI (latest version) -> Requirements: Docker + python 2.7 (aliased as python)
sudo pip install --upgrade ipaddress && sudo apt -y install xterm && sudo git clone --recursive https://github.com/KatharaFramework/Kathara.git /opt/kathara

printf "\n#Kathara Config\nexport NETKIT_HOME=/opt/kathara/bin\nexport PATH=\$PATH:\$NETKIT_HOME" >> ~/.bashrc

export NETKIT_HOME=/opt/kathara/bin

export PATH=$PATH:$NETKIT_HOME

$NETKIT_HOME/install
