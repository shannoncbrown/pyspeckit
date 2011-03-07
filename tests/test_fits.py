import spectrum

sp = spectrum.Spectrum('sample_13CO.fits')

print "Does it have an axis? ",sp.plotter.axis
sp.plotter()
print "How about now? ",sp.plotter.axis


# set the baseline to zero to prevent variable-height fitting
# (if you don't do this, the best fit to the spectrum is dominated by the
# background level)
sp.baseline.order = 0
sp.specfit()
sp.plotter.figure.savefig('fits_gaussfit.png')
print "Guesses: ", sp.specfit.guesses
print "Best fit: ", sp.specfit.modelpars

# # Fit a baseline, excluding the velocities with data, and don't subtract it
# sp.baseline(exclude=[12000,98000],subtract=False)
# print "Baseline: ",sp.baseline.baselinepars
# print "Excludepix: ",sp.baseline.excludepix
# print "EQW: ",sp.specfit.EQW()

sp.specfit(interactive=True)
raw_input('Press enter to print guesses and best fit and end code')
print "Guesses: ", sp.specfit.guesses
print "Best fit: ", sp.specfit.modelpars

print "EQW: ",sp.specfit.EQW()


#from matplotlib import pyplot

