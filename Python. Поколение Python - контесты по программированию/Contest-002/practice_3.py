class Algo:
    def __init__(self, n, m) -> None:
        self.__algo(n, m)

    def __algo(self, n, m):
        hovard = n
        vins = m
        grandmother = int(0)
        trap_hovard = int()
        trap_vins = int()
        step_hovard = 1 if 0 <= n else -1
        step_vins = 1 if 0 <= m else -1
        step_grandmother = 2 if 0 <= min(hovard, vins) else -2

        while True:
            hovard += step_hovard
            vins += step_vins
            grandmother += step_grandmother
            if hovard == grandmother:
                trap_hovard = grandmother
                break
            elif vins == grandmother:
                trap_vins = grandmother
                break

        # print('hovard = ', hovard)
        # print('vins = ', vins)
        # print('grandmother = ', grandmother)
        # print('trap_hovard = ', trap_hovard)
        # print('trap_vins = ', trap_vins)

        trap_end = int()
        hovard_or_vins = hovard if not hovard == trap_hovard else vins
        step_hovard_or_vins = 1 if 0 <= hovard_or_vins else -1
        step_grandmother = 2 if 0 <= hovard_or_vins else -2

        while True:
            hovard_or_vins += step_hovard_or_vins
            grandmother += step_grandmother
            if hovard_or_vins == grandmother:
                trap_end = grandmother
                break

        # print('hovard_or_vins = ', hovard_or_vins)
        # print('grandmother = ', grandmother)
        # print('trap_end = ', trap_end)

        trap_1 = int()
        trap_2 = int()
        trap_1 = trap_hovard if trap_hovard else trap_vins
        if 0 > trap_1:
            trap_2 = abs(trap_1) + trap_end
        else:
            trap_2 = trap_end - trap_1
        res = abs(trap_1) + abs(trap_2)

        # print('trap_1 = ', trap_1)
        # print('trap_2 = ', trap_2)
        # print('res = ', res)

        print(res)

if __name__ == '__main__':
    Algo(*list(map(int, input().split())))