import sys
n_s = int(sys.stdin.readline())
f_l = list(sys.stdin.readline().split())
s_l = list(sys.stdin.readline().split())
partner = {}
final = ()
for i in range(n_s):
    partner[f_l[i]] = s_l[i]
    if s_l[i] in partner.keys():
        if partner[s_l[i]] == f_l[i] and partner[s_l[i]] != s_l[i]:
            continue
        else:
            final = "bad"
            break
    final = "good"
print (final)


