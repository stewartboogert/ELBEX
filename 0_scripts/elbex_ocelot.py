import numpy as _np
import matplotlib.pyplot as _plt
import ocelot as _ocl
import pybdsim as _bd

def runOcelot(ocelotInput, emit_x=3.58e-11, emit_y=3.58e-11):
    tws0 = ocelotInput.tws0
    tws0.emit_x = emit_x
    tws0.emit_y = emit_y
    lat = _ocl.MagneticLattice(ocelotInput.cell)
    tws = _ocl.twiss(lat, tws0)
    return tws

def getDataFromList(List, param):
    l = []
    for elem in List:
        l.append(getattr(elem, param))
    return _np.array(l)


def plotAllResults(tws, ocelotInput, bdsimpath=None):
    plotBeta(tws, bdsimpath=bdsimpath)
    plotAlpha(tws, bdsimpath=bdsimpath)
    plotDisp(tws, bdsimpath=bdsimpath)
    plotSigma(tws, bdsimpath=bdsimpath)
    plotR56(tws, ocelotInput, bdsimpath=bdsimpath)
    plotK1(tws, ocelotInput, bdsimpath=bdsimpath)


def plotR56(tws, ocelotInput, label='R56', unit='mm', factor=1e3, bdsimpath=None,
            figsize=[12, 3], xlim=None, ylim=None):
    lat = _ocl.MagneticLattice(ocelotInput.cell)
    B, R, T, S = lat.transfer_maps(ocelotInput.tws0.E, output_at_each_step=True)
    RR = _np.asarray(R)

    _plt.figure(figsize=figsize)
    _plt.plot(S, RR[:, 4, 5] * factor, '-', color='C0', label=r'${}$'.format(label))
    _plt.ylabel(r'${}$ [{}]'.format(label, unit))
    _plt.xlabel(r'$s$ [m]')
    _plt.grid(True)
    _plt.legend()
    _plt.ylim(ylim)
    if bdsimpath is not None:
        _bd.Plot.AddMachineLatticeFromSurveyToFigure(_plt.gcf(), bdsimpath)
    _plt.xlim(xlim)


def plotK1(tws, ocelotInput, label='K1', unit='m$^{-2}$', factor=1, bdsimpath=None,
           figsize=[12, 3], xlim=None, ylim=None, width=2):
    s = []
    for elem in ocelotInput.cell:
        found = False
        for tw in tws:
            if tw.id == elem.id and found is False:
                s.append(tw.s)
                found = True
    K1 = getDataFromList(ocelotInput.cell, 'k1')

    _plt.figure(figsize=figsize)
    _plt.bar(s, K1 * factor, color='C0', label=r'${}$'.format(label), width=width)
    _plt.ylabel(r'${}$ [{}]'.format(label, unit))
    _plt.xlabel(r'$s$ [m]')
    _plt.grid(True)
    _plt.legend()
    _plt.ylim(ylim)
    if bdsimpath is not None:
        _bd.Plot.AddMachineLatticeFromSurveyToFigure(_plt.gcf(), bdsimpath)
    _plt.xlim(xlim)


def plotBeta(tws, unit='m', factor=1, **args):
    plotTwissXYAlongS(tws, x='beta_x', y='beta_y', label=r'\beta', unit=unit, factor=factor, **args)


def plotAlpha(tws, unit='rad', factor=1, **args):
    plotTwissXYAlongS(tws, x='alpha_x', y='alpha_y', label=r'\alpha', unit=unit, factor=factor, **args)


def plotDisp(tws, unit='m', factor=1, **args):
    plotTwissXYAlongS(tws, x='Dx', y='Dy', label=r'\eta', unit=unit, factor=factor, **args)


def plotSigma(tws, unit=r'$\mu m$', factor=1e6, **args):
    plotTwissXYAlongS(tws, x='sigma_x', y='sigma_y', label=r'\sigma', unit=unit, factor=factor, **args)


def plotTwissXYAlongS(tws, x='beta_x', y='beta_y', label=r'\beta', unit='m', factor=1,
                      xlim=None, ylim=None, bdsimpath=None, figsize=[12, 3]):
    s_tws = getDataFromList(tws, 's')
    x_tws = getDataFromList(tws, x)
    y_tws = getDataFromList(tws, y)

    _plt.figure(figsize=figsize)
    _plt.plot(s_tws, x_tws*factor, '-', color='C0', label=r'${}_x$'.format(label))
    _plt.plot(s_tws, y_tws*factor, '-', color='C1', label=r'${}_y$'.format(label))
    _plt.ylabel(r'${}$ [{}]'.format(label, unit))
    _plt.xlabel(r'$s$ [m]')
    _plt.grid(True)
    _plt.legend()
    _plt.ylim(ylim)
    if bdsimpath is not None:
        _bd.Plot.AddMachineLatticeFromSurveyToFigure(_plt.gcf(), bdsimpath)
    _plt.xlim(xlim)