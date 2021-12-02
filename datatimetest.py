from datetime import datetime ,timedelta,timezone
import re

def to_timestamp(dt_str,tz_str):
    realtime=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    rl_tz=re.match(r'UTC(.*):',tz_str).group(1)
    rl_inttz=int(rl_tz)
    #print (rl_tz)
    utc_dt=realtime.replace(tzinfo=timezone(timedelta(hours=rl_inttz)))
    return utc_dt.timestamp()










t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')