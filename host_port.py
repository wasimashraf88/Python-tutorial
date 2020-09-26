for host_port in range(0, 50):
    ip_address = "192.168.0." + str(host_port)
    if host_port >= 1 and host_port <= 20:
        print(ip_address + " is reseverd!")
    else:
        print(ip_address + " is available")
    
    