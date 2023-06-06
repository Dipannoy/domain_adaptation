import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


#OQMD_hf,DFT_hf,DFT_corrected_hf

df_plot=pd.read_csv('formation_energy_comparison_summary.csv')
calc_eigs=['DFT_hf','DFT_corrected_hf']
calc_labels=['err_DFT','err_corrected_DFT']

for i in range (len(calc_eigs)):
    df_plot[str(calc_labels[i])]=df_plot.OQMD_hf-df_plot[calc_eigs[i]]
#df_plot=df_plot[calc_labels]

figsize=(9,5);axis_width=2

fig, ax = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=True, figsize=figsize)
fontsize=23
ylab='dHf error (eV)'   
plt.grid(zorder=100)
sns.violinplot(data=df_plot,linewidth=2.5)
sns.set_theme(style = 'white',palette = 'colorblind') 
sns.set_style("ticks")
plt.ylabel(ylab, fontsize=fontsize)

plt.legend(fontsize=fontsize-2,frameon=False)
axis_width=1.5
plt.subplots_adjust(left=0.15,bottom=0.1,top=0.97,right=0.97)
plt.tick_params('both', length = 6, width = axis_width, which = 'major',right=True,top=False,bottom=True)
plt.yticks(fontsize=fontsize)
plt.xticks(fontsize=fontsize,rotation=0)
plt.xlabel('',fontsize=fontsize*0.0)
plt.ylim(-0.4,0.2)
plt.savefig('error_distribution.png',dpi=150)
plt.show()

plt.close()
