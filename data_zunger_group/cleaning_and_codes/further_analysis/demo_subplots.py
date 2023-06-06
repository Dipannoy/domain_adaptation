import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


#OQMD_hf,DFT_hf,DFT_corrected_hf

df_plot=pd.read_csv('optimized_formation_energy_comparison_summary.csv')
#'''
calc_eigs=['DFT_corrected_hf']
calc_labels=['Calculated dhf']
for i in range (len(calc_eigs)):
    df_plot[str(calc_labels[i])]=df_plot.OQMD_hf-df_plot[calc_eigs[i]]
#df_plot=df_plot[calc_labels]
#print(df_plot.columns)
#'''
label_pp=['pp_match','pp_match','pp_mismatch','pp_mismatch']
label_mag=['Non-magnetic','Magnetic','Non-magnetic','Magnetic']

figsize=(9,5);axis_width=2
nrow=2;ncol=2
fig, ax = plt.subplots(nrows=nrow, ncols=ncol, sharex=False, sharey=True, figsize=figsize)
fontsize=14
for i in range (1,nrow+ncol+1,1):
    xlabel='Calculated dhf'
    plt.subplot(nrow,ncol,i)
    ylab='dHf error (eV)'   
    plt.grid(zorder=100)
    data=df_plot[(df_plot.POTCAR==label_pp[i-1])&(df_plot.SPIN==label_mag[i-1])]
    a,b=data.shape
    #print(data.columns)
    sns.violinplot(y=data[xlabel],linewidth=2.5)
    mae1=abs(data[xlabel]).mean()
    mae="{:.3f}".format(mae1)
    sns.set_theme(style = 'white',palette = 'colorblind') 
    sns.set_style("ticks")
    plt.ylabel(ylab, fontsize=fontsize)

    axis_width=1.5
    plt.subplots_adjust(left=0.15,bottom=0.1,top=0.97,right=0.97)
    plt.tick_params('both', length = 6, width = axis_width, which = 'major',right=False,top=False,bottom=True)
    plt.yticks(fontsize=fontsize)
    plt.xticks(fontsize=fontsize,rotation=0)
    plt.xlabel(xlabel,fontsize=fontsize)
    #plt.ylim(-0.4,0.2)
    plt.title(str(label_mag[i-1])+'_'+str(label_pp[i-1])+'_'+str(mae)+'_Tot_Comp='+str(a),fontsize=fontsize-1)
plt.tight_layout()
#plt.legend(fontsize=fontsize-2,frameon=False)
plt.savefig('error_distribution_optimized_calcs.png',dpi=150)
plt.show()

plt.close()
