from ppadb.client import Client as AdbClient


def read_otp_from_phone():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    # Execute ADB shell command to retrieve the latest OTP message
    command = "content query --uri content://sms/inbox --projection body --where \"body LIKE '% AJIO %'\""
    result = device.shell(command)

    otps = []

    # Process the command output to extract OTPs
    for line in result.splitlines():
        if "body=" in line:
            otp = line.split("=")[1].strip()
            otps.append(otp)

    # Print the OTPs
    
    return otps[0]

    # device.close()