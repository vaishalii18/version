import argparse
LIMIT=argparse.Argumentparser
LIMIT.add_argument('limit',type=int)
args=LIMIT.parse_args()
Limit=args.limit
l=[]
if Limit == 0:
    print("0")
elif Limit == 1:
    print(" 0 \n 1")
else:
        l.append(0)
        l.append(1)
        for i in range(2,Limit+1):
            item=l[i-1]+l[i-2]
            l.append(item)

print("fibonacci series: \n " +str())

