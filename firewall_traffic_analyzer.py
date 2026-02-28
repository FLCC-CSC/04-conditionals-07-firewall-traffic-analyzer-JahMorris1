# FILE NAME - firewall_traffic_analyzer.py

# NAME: Jahni Morris
# DATE: February 28th, 2026
# BRIEF DESCRIPTION:  Write a program that considers two pieces of data and makes a risk analysis.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("=== Network Traffic Security Analyzer ===")
print()

port_number = int(input("Enter the port number (e.g.. 80, 22, 443, 3389): "))
transfer_size = int(input("Enter the data transfer size in megabytes (MB): "))

#Risk analysis
if (port_number == 22 or port_number == 3389) and transfer_size >= 100:
    risk = "HIGH RISK: Potential_unauthoried remote access detected!"
elif port_number == 80 and transfer_size > 100:
    risk = "MEDIUM RISK: Large unencrypted data transfer detected."
elif port_number == 443:
    risk = "LOW RISK: Secure encrypted transfer detected."
else:
    risk = "UNKNOWN: Unrecognized traffic pattern."

print()
print("FIREWALL LOG:")
print(f"Port: {port_number}, Transfer Size: {transfer_size} MB")
print(f"Risk Assessment: {risk}")
print("------------------------")               









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 12

FIREWALL LOG:
Port: 22, Transfer Size: 12 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?
Yes I did get trripped up a little using the "or" and "and" operators at first. I was confused at understanding how they worked together in the same condtion but i had to remember that "and" is higher than "or" in Python, so it gets evaluated first.






'''
