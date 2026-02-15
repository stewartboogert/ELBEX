import matplotlib.pyplot as _plt 

def plotTwissXYAlongS(tws, line = 'XTD8', y1='betx', y2='bety', label=r'\beta', unit='m', factor=1,
                      xlim=None, ylim=None, bdsimpath=None, figsize=[12, 3]):
    s = tws[line]['s']
    y1 = tws[line][y1]
    y2 = tws[line][y2]

    _plt.figure(figsize=figsize)

    _plt.plot(s, y1*factor, '-', color='C0', label=r'${}_x$'.format(label))
    _plt.plot(s, y2*factor, '-', color='C1', label=r'${}_y$'.format(label))

    _plt.ylabel(r'${}$ [{}]'.format(label, unit))
    _plt.xlabel(r'$s$ [m]')
    _plt.grid(True)