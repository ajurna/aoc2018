import re
import string

with open('01.txt', 'r') as f:
    data_orig = f.read().strip()

reg = re.compile(r'(aA|bB|cC|dD|eE|fF|gG|hH|iI|jJ|kK|lL|mM|nN|oO|pP|qQ|rR|sS|tT|uU|vV|wW|xX|yY|zZ|Aa|Bb|Cc|Dd|Ee|Ff'
                 r'|Gg|Hh|Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp|Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx|Yy|Zz)')

data = data_orig
while True:
    match = reg.findall(data)
    if not match:
        break
    for pat in match:
        data = data.replace(pat, '', 1)
print('Part 1:', len(data))

pairs = list(zip(string.ascii_lowercase, string.ascii_uppercase))

results = []
for pair in pairs:
    data = data_orig
    data = data.replace(pair[0], '')
    data = data.replace(pair[1], '')
    while True:
        match = reg.findall(data)
        if not match:
            break
        for pat in match:
            data = data.replace(pat, '', 1)
    results.append((len(data), pair))
results.sort()

print('Part 2:', results.pop(0)[0])
