import sys
channel = int(input())
malfunc = int(input())
least = abs(100- channel)
if malfunc != 0:
    buttons = list(map(str,input().split()))
else:
    print(min(least,len(str(channel))))
    sys.exit()
channels = [x for x in range(0,1000000) if not any((b in buttons) for b in str(x))]

if len(channels) == 0:
    print(least)
    sys.exit()
for c in channels:
    least = min(least, abs(channel -c) + len(str(c)))
print(least)