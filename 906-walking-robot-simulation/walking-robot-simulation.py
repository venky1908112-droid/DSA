class Solution(object):
    def robotSim(self, commands, obstacles):
        obs = set(map(tuple,obstacles))
        directions = {
            'n'  : {-1 : 'e', -2 : 'w'},
            's'  : {-1 : 'w', -2 : 'e'},
            'e'   : {-1 : 's', -2 : 'n'},
            'w'   : {-1 : 'n', -2 : 's'}
        }
        ans = 0
        x,y = 0,0
        curr_d = 'n'
        for command in commands:
            if command < 0:
                curr_d = directions[curr_d][command]
            else:
                for _ in range(command):
                    nx, ny = x, y
                    if curr_d == 'n':
                        ny += 1
                    elif curr_d == 's':
                        ny -= 1
                    elif curr_d == 'e':
                        nx += 1
                    else:
                        nx -= 1
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                ans = max(ans, x*x + y *y)
        return ans

        