class Solution(object):
    def robotSim(self, commands, obstacles):
        obs = set(map(tuple, obstacles))
        directions = {
            'North' : {-1 : 'East', -2 : 'West'},
            'South' : {-1 : 'West', -2 : 'East'},
            'East'  : {-1 : 'South', -2 : 'North'},
            'West'  : {-1 : 'North', -2 : 'South'}
        }
        x,y = 0,0
        curr_d = 'North'
        ans = 0
        for command in commands:
            if command <= 0:
                curr_d = directions[curr_d][command]
            else:
                for _ in range(command):
                    nx, ny = x, y
                    if curr_d == 'North':
                        ny += 1
                    elif curr_d == 'South':
                        ny -= 1
                    elif curr_d == 'East':
                        nx += 1
                    else:
                        nx -= 1
                    if (nx,ny) in obs:
                        break
                    x, y = nx, ny
                ans = max(ans, x*x + y*y)
        return ans