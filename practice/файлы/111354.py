file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
x = lines.index('VOTES:\n')
parties, votes, ans = lines[1:x], lines[x+1:], ''
votes_cnt, all_votes = [votes.count(i) for i in parties], len(votes)
for i, partia in enumerate(parties):
    if (votes_cnt[i] / all_votes) * 100 >= 7:
        ans +=  partia
output_file.write(ans)