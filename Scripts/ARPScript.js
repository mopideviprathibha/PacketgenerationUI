function validateARPDetails(){
    var destinationIP = document.forms["arp-form"]["destinationIP"].value;
    var destinationMAC = document.forms["arp-form"]["destinationMAC"].value;
    var sourceIP = document.forms["arp-form"]["sourceIP"].value;

    if(!destinationIP){
        alert('please enter destinationIP');
        return false;
    }
    if(!destinationMAC){
        alert('please enter destinationMAC');
        return false;
    }
    if(!sourceIP){
        alert('please enter sourceIP');
        return false;
    }

    var regex = /^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/

    if(!regex.test(destinationIP)){
        alert('Destination IP address should be in this format - [0-255].[0-255].[0-255].[0-255]');
        return false;
    }
    if(!regex.test(sourceIP)){
        alert('Source IP address should be in this format - [0-255].[0-255].[0-255].[0-255]');
        return false;
    }
    
    return true;
}