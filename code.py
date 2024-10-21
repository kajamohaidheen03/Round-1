def non_repeating_char(s):

for i in range(len(s)): char = True

for j in range(len(s)): if i != j and s[i] == s[j]: char = False break

if char: return s[i]

return None

input_s = input() res = non_repeating_char(input_s) if res: print(res) else: print("No non-repeating character found")
