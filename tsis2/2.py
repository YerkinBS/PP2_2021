class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        i = 0
        while True:
            if i - 1 == len(command):
                break
            if command[i] == 'G':
                ans += 'G'
            elif command[i] == '(' and command[i+1] == ')':
                ans += 'o'
                if i + 2 < len(command):
                    i += 2
                    continue
                else:
                    break
            else:
                ans += 'al'
                if(i + 4 < len(command)):
                    i += 4
                    continue
                else:
                    break
            if i + 1 < len(command):
                i += 1
            else:
                break
        return(ans)