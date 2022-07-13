# helpers for plotting 

import matplotlib.pyplot as plt

class PSFhelpers:
    def show(psf, gamma=0.5):
        plt.imshow(psf**gamma)
        plt.colorbar()
    
    def showWithPspec(psf, gammaPSF=0.5, gammaPSpec=0.2):
        pspec = np.abs(np.fft.fftshift((np.fft.fft2(psf))))
        plt.subplot(1,2,1)
        plt.imshow(psf**gammaPSF)
        plt.colorbar()
        plt.subplot(1,2,2)
        plt.imshow(pspec**gammaPSpec)
        plt.colorbar()

    def comparePspec(psf1, psf2):
        pspec1 = np.abs(np.fft.fftshift((np.fft.fft2(psf1))))
        pspec2 = np.abs(np.fft.fftshift((np.fft.fft2(psf2))))
        plt.imshow(pspec1/(pspec2),vmin=0.5,vmax=2)
        plt.colorbar()


# taken from https://github.com/nackjaylor/formatting_tips-tricks/blob/main/python/format_figures.py
def startup_plotting(font_size=16,line_width=1.5,output_dpi=300,tex_backend=False):

    if tex_backend:
        try:
            plt.rcParams.update({
                    "text.usetex": True,
                    "font.family": "serif",
                    "font.serif": ["Computer Modern Roman"],
                        })
        except:
            print("WARNING: LaTeX backend not configured properly. Not using.")
            plt.rcParams.update({"font.family": "serif",
                    "font.serif": ["Computer Modern Roman"],
                        })
    
    # TODO: Colour-scheme.

    # Turn on axes grids.
    plt.rcParams.update({"axes.grid" : True, 
                        "legend.framealpha": 1,
                        "legend.edgecolor": [1,1,1],
                        "lines.linewidth": line_width,
                        "savefig.dpi": output_dpi,
                        "savefig.format": 'pdf'})

    # Change default font sizes.
    plt.rc('font', size=font_size) #controls default text size
    plt.rc('axes', titlesize=font_size) #fontsize of the title
    plt.rc('axes', labelsize=font_size) #fontsize of the x and y labels
    plt.rc('xtick', labelsize=font_size) #fontsize of the x tick labels
    plt.rc('ytick', labelsize=font_size) #fontsize of the y tick labels
    plt.rc('legend', fontsize=0.85*font_size) #fontsize of the legend 



