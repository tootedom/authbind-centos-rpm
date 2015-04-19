
$script = <<SCRIPT
yum install rpm-build -y
yum install rpmdevtools rpmlint -y
yum install gcc-c++ -y
rpmdev-setuptree
rm -rf /root/rpmbuild
ln -s /vagrant/authbind/ /root/rpmbuild
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
yum install git -y
yum install yum-utils -y
yum install java -y
cd /root/rpmbuild/
yum-builddep SPECS/authbind.spec -y
# This will build the authbind rpm
#rpmbuild -v -bb --clean SPECS/authbind.spec
SCRIPT

$rootforwarding = <<ROOTFWD
# allow agent forwarding to be available into sudo -i
echo "Defaults    env_keep += \"SSH_AUTH_SOCK\"" > /etc/sudoers.d/root_ssh_agent
ROOTFWD

Vagrant.configure("2") do |config|
  config.vm.define "authbind-vm" do |conf|

    # use ssh agent forwarding for local ssh user to be used by vms (i.e. git access)
    conf.ssh.forward_agent = true
    conf.vm.box = "chef/centos-6.5"

    conf.vm.provider :virtualbox do |virtualbox|
      virtualbox.customize ["modifyvm", :id, "--memory", "512"]
      virtualbox.customize ["modifyvm", :id, "--cpus", "2"]
      virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 10000 ]
    end

    conf.vm.provision :shell, inline: $rootforwarding
    conf.vm.provision :shell, inline: $script

  end
end
