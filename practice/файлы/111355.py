def cmp(x):
    return (len(votes) - x[1], x[0])
    
file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
x, d, ans = lines.index('VOTES:\n'), {}, ''
parties, votes, ans = lines[1:x], lines[x+1:], ''
votes_cnt = [votes.count(i) for i in parties]
for i in range(len(parties)): d[parties[i]] = votes_cnt[i]
for key, value in sorted(d.items(), key=cmp): ans += key
output_file.write(ans)