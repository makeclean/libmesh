#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

"""
This script creates a bar graph of the number of "papers using libmesh" by year.

* We do not simply count citations, the authors must have actually
  used libmesh in part of their work.
* Conversely, not everyone who uses libmesh actually cites it, for
  example when it is used through another library or application. We
  also include such papers in this list.
* This data can be regenerated by running the ./create_website.sh
  script in the doc/citations directory.
* The yearly citations can include anything (conference papers,
  technical reports, etc.) that is not a dissertation/thesis, as those
  are counted in a separate category.
* The libmesh paper came out in 2006, but there are some citations
  prior to that date which mainly referred to the old libmesh.sf.net
  site at the time.
"""

# These counts can be generated from the latest Bibtex files by
# running "./create_website.sh -c" in the doc/citations
# directory. Note: you must have bibtex2html in your PATH in order to
# run this script.
data = [
'\'04', 5,
'\'05', 2,
'\'06', 14,
'\'07', 8,
'\'08', 23,
'\'09', 29,
'\'10', 26,
'\'11', 34,
'\'12', 56,
'\'13', 82,
'\'14', 74,
'\'15', 94,
'\'16', 125,
'\'17', 133,
'\'18', 149,
'\'19', 123,
'\'20', 34,
'T', 115,
    ]

# Extract the x-axis labels from the data array
ticklabels = data[0::2]

# Extract the publication counts from the data array
n_papers = data[1::2]

# The number of data points
N = len(ticklabels);

# Get a reference to the figure
fig = plt.figure()

# 111 is equivalent to Matlab's subplot(1,1,1) command
ax = fig.add_subplot(111)

# Create an x-axis for plotting
x = np.linspace(1, N, N)

# Width of the bars
width = 0.8

# Make the bar chart.
# The colors used come from sns.color_palette("muted").as_hex() They
# are the "same basic order of hues as the default matplotlib color
# cycle but more attractive colors."
ax.bar(x[0:N-1], n_papers[0:N-1], width, color=u'#4878cf', align='center')
ax.bar(x[-1],    n_papers[-1],    width, color=u'#6acc65', align='center')

# Label the x-axis
plt.xlabel('T=PhD, MS, and BS Theses')

# Set up the xtick locations and labels.  Note that you have to offset
# the position of the ticks by width/2, where width is the width of
# the bars.
ax.set_xticks(np.linspace(1,N,N))
ax.set_xticklabels(ticklabels)
ax.tick_params(direction='out')
ax.set_xlim([0,N+1])

# Create a title string
title_string = 'Papers by People Using LibMesh, (' + str(sum(n_papers)) + ' Total)'
fig.suptitle(title_string)

# Save as PDF
plt.savefig('libmesh_citations.pdf')

# Local Variables:
# python-indent: 2
# End:
