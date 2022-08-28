d = int(input())
Oc, Of, Od = map(int, input().split())
Cs, Cb, Cm, Cd = map(int, input().split())

online_cost = Oc + Od * (d - Of)

classic_cost = Cb + Cm * (d/Cs) + Cd * d

if online_cost <= classic_cost:
    print("Online Taxi")
else:
    print("Classic Taxi")
