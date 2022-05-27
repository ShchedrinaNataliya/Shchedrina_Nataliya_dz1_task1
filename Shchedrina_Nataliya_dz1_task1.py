# Задача № 1
duration = int(input('Enter the number of seconds '))
seconds = duration % (24 * 3600)
hours = seconds // 3600
seconds = duration % 3600
minutes = seconds // 60
seconds = duration % 60
days = duration // 86400
if duration < 60:
    print('Time', ':', seconds, 'sec')
if duration >= 60 and duration < 3600:
    print('Time', ':', minutes, 'min', seconds, 'sec')
if duration >= 3600 and duration < 86400:
    print('Time', ':', hours, 'h', minutes, 'min', 'and', seconds, 'sec')
if duration >= 86400:
    print('Time', ':', days, 'd', hours, 'h', minutes, 'min', 'and', seconds, 'sec')
