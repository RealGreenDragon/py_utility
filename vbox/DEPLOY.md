# VirtualBox Configuration Guide for Ubuntu and derivates

Author: Daniele Giudice

## Install/Update VirtualBox Guest Additions + Enable Shared Folders Access

#### Update all packages + Install 'VirtualBox Guest Additions' dependencies
sudo apt -y update && sudo apt -y upgrade && sudo apt -y install build-essential virtualbox-guest-dkms linux-headers-virtual && sudo apt -y clean && sudo apt -y autoremove --purge

#### Mount 'Guest Additions CD' from menu "Devices->Insert Guest Additions CD image..."

#### Install/Update Guest Additions
sudo "$(df --output=target | grep VBox_GAs_)/VBoxLinuxAdditions.run"

#### Unmount 'Guest Additions CD'
sudo umount -f "$(df --output=target | grep VBox_GAs_)"

#### Remove 'Guest Additions CD' by right click on disk icon in vbox windows bottom-right and select "Remove disk from virtual drive"

#### Add current user in 'vboxsf' group to grant access to shared folders
sudo usermod --append --groups vboxsf $(whoami)

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
sudo apt install -y net-tools unrar ffmpeg && sudo apt -y clean && sudo apt -y autoremove --purge

#### Notepadqq
sudo add-apt-repository -y ppa:notepadqq-team/notepadqq && sudo apt -y update && sudo apt install -y notepadqq && sudo apt -y clean && sudo apt -y autoremove --purge

#### Atom
sudo wget -O ~/atom-amd64.deb https://atom.io/download/deb && sudo apt -y install ~/atom-amd64.deb && sudo apt -y clean && sudo apt -y autoremove --purge && sudo rm -rf ~/atom-amd64.deb

#### XAMPP v7.3.2 x64
sudo wget -O ~/xampp-x64.run "https://www.apachefriends.org/xampp-files/7.3.2/xampp-linux-x64-7.3.2-1-installer.run" && sudo chmod +x ~/xampp-x64.run && sudo ~/xampp-x64.run --mode unattended && sudo rm -rf ~/xampp-x64.run && sudo chmod a+x -R /opt/lampp/htdocs/

sudo /opt/lampp/manager-linux-x64.run **(Start XAMPP Manager)**

sudo /opt/lampp/lampp start **(Start All XAMPP Services)**
