from datetime import datetime

now = datetime.now()
test = datetime(2022,12,24)
time = test - now
left = time.days

print("%3d days(include today but last) until the 2023 Graduate Entrance Examination."%left)
