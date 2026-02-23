import matplotlib.pyplot as _plt 
import pandas as _pd

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

def writeXsuiteToExcel(xsuite, outputfilename, scut=None):
    df = buildDF(xsuite, scut=scut)
    df.to_excel(outputfilename)


def buildDF(xsuite, scut=None):
    survey = xsuite.env.XTD8.survey(**xsuite.surv0)

    df = _pd.DataFrame()
    for coord in ['name', 'X', 'Y', 'Z', 'theta', 'phi', 'psi', 'angle']:
        df[coord] = getattr(survey, coord)
    T = []
    for t in survey.element_type:
        if t == 'Drift':
            T.append('DRIF')
        elif t == 'Marker' or t == '':
            T.append('MARK')
        elif t == 'RBend':
            T.append('RBEN')
        elif t == 'SBend' or t == 'Bend':
            T.append('SBEN')
        elif t == 'Quadrupole':
            T.append('QUAD')
        elif t == 'Sextupole':
            T.append('SEXT')
        else:
            print('type : ', t)
    df['TYPE'] = T
    df['L'] = survey.length

    df_mag = df[df.TYPE.isin(['RBEN', 'SBEN', 'QUAD', 'SEXT', 'MARK'])]

    CLASS = []
    for name in df_mag.name:
        CLASS.append(name.split('.')[0])
    df_mag['CLASS'] = CLASS

    if scut is not None:
        df_mag = df_mag[df_mag.s >= scut]

    K1 = []
    for name in df_mag.name:
        try:
            K1.append(xsuite.env[name].k1)
        except:
            K1.append(0)
    df_mag['K1'] = K1
    df_mag['STRENGH'] = df_mag['K1'] * df_mag['L']

    df_mag = df_mag.rename(columns={'name': 'NAME'})
    df_mag = df_mag.rename(columns={'angle': 'ANGLE'})
    df_mag = df_mag.rename(columns={'theta': 'THETA'})
    df_mag = df_mag.rename(columns={'phi': 'PHI'})
    df_mag = df_mag.rename(columns={'psi': 'PSI'})

    df_mag = df_mag[['NAME', 'TYPE', 'CLASS', 'X', 'Y', 'Z', 'THETA', 'PHI', 'PSI', 'L', 'ANGLE', 'K1', 'STRENGH']]

    return df_mag