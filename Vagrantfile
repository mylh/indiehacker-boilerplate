# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  config.vm.define "{{ project_name }}_vagrant" do |{{ project_name }}|
    {{ project_name }}.vm.box = "ubuntu/jammy64"
    {{ project_name }}.vm.network "private_network", ip: "192.168.56.10"
  end

  # config.vm.box_check_update = false
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "public_network"
  # config.vm.synced_folder "../data", "/vagrant_data"
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "2096"
    vb.cpus = 1
  end
end
