### WEEK 2 - TUTORIAL 2
 # SCENARIO
 # A movie theatre has the following admissuon policy. A person # is allowed to enter if:
 # - users are 13 years old, OR
 # - users are accompanied by an adult
 # - users must have a valid ticket 

# ACTIVITY
# 1. identify the components
# inputs
- age
- accompanied by an adult (yes/no)
- have valid ticket (yes/no)

# process
- check if users are older than 13 years old or younger
- check if users who are younger than 13 years old are accompanied by an adult
- check if users have a valid ticket

# output
- Admission Approved 
- Admission Denied

# 2. Design the algorithm
Admission approved = users age >/ 13 OR accompanied by an adult AND have valid ticket

# flowchart

![alt text](image.png)

# truth table 

| Age >/ 13 | With Adult | Has Ticket | Admission approved |
|----------|----------|----------|----------|
| False | False | False | False |
| False | False | True | False |
| False | True | False | False |
| False | True | True | True |
| True | False | False | False |
| True | True | True | True |
| True | True | False | False |
| True | False | True | True |

# step by step
1. Start
2. Input age.
3. Input whether accompanied by an adult (yes/no)
4. Input whether the ticket is valid.
5. If (Age ≥ 13 OR Accompanied by Adult) AND Valid Ticket:
Display "Admission Granted"
Else:
Display "Admission Denied"
7. End

# pseudocode
BEGIN 
INPUT age 
INPUT accompaniedByAdult 
INPUT validTicket 
IF ((age >= 13 OR accompaniedByAdult = TRUE) AND validTicket = TRUE) 
THEN DISPLAY "Admission Approved" 
ELSE DISPLAY "Admission Denied" 
END IF