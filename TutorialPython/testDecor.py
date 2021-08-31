from RastrWinLib.tools.timer import timethis


@timethis
def countdown(n):
    """

    :param n:
    :return:
    """
    while n > 0:
        # print(n)
        n = n - 1


countdown(1000000)
