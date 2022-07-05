# Terraform Azure

## Azure CLi setup
```
# mkdir azure_cli && cd $_
# echo -e "[azure-cli]
name=Azure CLI
baseurl=https://packages.microsoft.com/yumrepos/azure-cli
enabled=1
gpgcheck=1
gpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/azure-cli.repo

# yum install -y azure-cli
# az upgrade
# az --version
# az login
# resourceGroup=VMTutorialResources
# location=koreacentral
# az group create --name $resourceGroup --location $location
# vnetName=TutorialVNet1
# subnetName=TutorialSubnet1
# vnetAddressPrefix=10.126.0.0/16
# subnetAddressPrefix=10.126.0.0/24
```

## Azure Cli Vnet(VPC) Create
```
# az network vnet create \
--name $vnetName \
--resource-group $resourceGroup \
--address-prefixes $vnetAddressPrefix \
--subnet-name $subnetName \
--subnet-prefixes $subnetAddressPrefix

# az network vnet list
```

## Azure Cli VM Create
```
# az vm image list
# vmName=TutorialVM1
# vi httpd.txt
#!/bin/bash
apt update
apt install -y apache2
echo "<h1>Hello Azure CLI</h1>" > /var/www/html/index.html

# az vm create \
--resource-group $resourceGroup \
--name $vmName \
--image UbuntuLTS \
--vnet-name $vnetName \
--subnet $subnetName \
--size Standard_B1s \
--custom-data httpd.txt \
--admin-username azureuser \
--generate-ssh-keys \
--output json \
--verbose

# az network nsg rule create \
--resource-group $resourceGroup \
--nsg-name TutorialVM1NSG \
--name myNetworkSecurityGroupRule \
--protocol tcp \
--priority 900 \
--destination-port-range 80

# az vm open-port -n $vmName -g $resourceGroup --port 443 --priority 999
# az vm list-ip-addresses
# ssh -i .ssh/id_rsa azureuser@20.214.201.208
# az vm delete --resource-group $resourceGroup --name $vmName --yes
# az group delete -n $resourceGroup
# az group delete -n NetworkWatcherRG
```

## Azure Terraform VPC/VM Create
```
# vi variables.tf
variable "resource_group_name_prefix" {
  default       = "rg"
  description   = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
}

variable "resource_group_location" {
  default = "koreacentral"
  description   = "Location of the resource group."
}

# vi main.tf
provider "azurerm" {
  features {}
}

resource "random_pet" "rg-name" {
  prefix    = var.resource_group_name_prefix
}

resource "azurerm_resource_group" "rg" {
  name      = random_pet.rg-name.id
  location  = var.resource_group_location
}

# Create virtual network
resource "azurerm_virtual_network" "myterraformnetwork" {
  name                = "myVnet"
  address_space       = ["10.226.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# Create subnet
resource "azurerm_subnet" "myterraformsubnet" {
  name                 = "mySubnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.myterraformnetwork.name
  address_prefixes     = ["10.226.0.0/24"]
}

# Create public IPs
resource "azurerm_public_ip" "myterraformpublicip" {
  name                = "myPublicIP"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Dynamic"
}

# Create Network Security Group and rule
resource "azurerm_network_security_group" "myterraformnsg" {
  name                = "myNetworkSecurityGroup"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  security_rule {
    name                       = "SSH"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "HTTP"
    priority                   = 1002
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "80"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

# Create network interface
resource "azurerm_network_interface" "myterraformnic" {
  name                = "myNIC"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "myNicConfiguration"
    subnet_id                     = azurerm_subnet.myterraformsubnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.myterraformpublicip.id
  }
}

# Connect the security group to the network interface
resource "azurerm_network_interface_security_group_association" "example" {
  network_interface_id      = azurerm_network_interface.myterraformnic.id
  network_security_group_id = azurerm_network_security_group.myterraformnsg.id
}

# Create (and display) an SSH key
resource "tls_private_key" "example_ssh" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Create virtual machine
resource "azurerm_linux_virtual_machine" "myterraformvm" {
  name                  = "myVM"
  location              = azurerm_resource_group.rg.location
  resource_group_name   = azurerm_resource_group.rg.name
  network_interface_ids = [azurerm_network_interface.myterraformnic.id]
  size                  = "Standard_B1s"

  os_disk {
    name                 = "myOsDisk"
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  computer_name                   = "myvm"
  admin_username                  = "azureuser"
  custom_data                     = filebase64("httpd-azure.txt")
  disable_password_authentication = true

  admin_ssh_key {
    username   = "azureuser"
    public_key = tls_private_key.example_ssh.public_key_openssh
  }

}

# vi outputs.tf
output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "public_ip_address" {
  value = azurerm_linux_virtual_machine.myterraformvm.public_ip_address
}

output "tls_private_key" {
  value     = tls_private_key.example_ssh.private_key_pem
  sensitive = true
}

# terraform init
# terraform plan
# terraform apply
# terraform output -raw tls_private_key > azure-key.pem
# terraform output public_ip_address
# chmod 400 azure-key.pem
# ssh -i azure-key.pem azureuser@<public_ip_address>
```