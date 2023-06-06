import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

df_plot=pd.read_csv('dft_predictions.csv')
print(df_plot.shape)
calc_eigs=['lat_BVM','hf_BVM','hf_ML']
act_eigs=['lat_opt','hf_opt','hf_opt']
calc_labels=['Lat_err','hf_BVM_err','hf_ML_err']

for i in range (len(calc_eigs)):
    df_plot[str(calc_labels[i])]=df_plot[act_eigs[i]]-df_plot[calc_eigs[i]]
df_plot1=df_plot[calc_labels[1:3]]
print(df_plot.shape)

def violin(df_plot):
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
    #plt.ylim(-0.4,0.2)
    plt.savefig('error_schNET.png',dpi=150)
    plt.show()

    plt.close()


def scatter_err(df_plot):
    figsize=(6,4);axis_width=2

    fig, ax = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=True, figsize=figsize)
    fontsize=23
    ylab='dHf error (eV)'
    plt.grid(zorder=100)
    sns.scatterplot(x=df_plot.Lat_err,y=df_plot.hf_BVM_err)
    sns.scatterplot(x=df_plot.Lat_err,y=df_plot.hf_ML_err)
    sns.set_theme(style = 'white',palette = 'colorblind')
    sns.set_style("ticks")
    plt.ylabel(ylab, fontsize=fontsize)

    plt.legend(['BVM_err','ML_err'],fontsize=fontsize-2,frameon=False)
    axis_width=1.5
    plt.subplots_adjust(left=0.2,bottom=0.2,top=0.97,right=0.97)
    plt.tick_params('both', length = 6, width = axis_width, which = 'major',right=True,top=False,bottom=True)
    plt.yticks(fontsize=fontsize)
    plt.xticks(fontsize=fontsize,rotation=0)
    plt.xlabel('Lattice constant error',fontsize=fontsize)
    #plt.ylim(-0.4,0.2)
    plt.savefig('error_schNET.png',dpi=150)
    plt.show()

    plt.close()

#scatter_err(df_plot)


def scatter(df_plot):
    figsize=(6,4);axis_width=2

    fig, ax = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=True, figsize=figsize)
    fontsize=23
    ylab='dHf (eV)'
    plt.grid(zorder=100)
    sns.scatterplot(x=df_plot.Lat_err,y=df_plot.hf_BVM)
    sns.scatterplot(x=df_plot.Lat_err,y=df_plot.hf_opt)
    sns.scatterplot(x=df_plot.Lat_err,y=df_plot.hf_ML)
    sns.set_theme(style = 'white',palette = 'colorblind')
    sns.set_style("ticks")
    plt.ylabel(ylab, fontsize=fontsize)

    plt.legend(['hf_BVM','hf_OPT','hf_ML'],fontsize=fontsize-2,frameon=False)
    axis_width=1.5
    plt.subplots_adjust(left=0.2,bottom=0.2,top=0.97,right=0.97)
    plt.tick_params('both', length = 6, width = axis_width, which = 'major',right=True,top=False,bottom=True)
    plt.yticks(fontsize=fontsize)
    plt.xticks(fontsize=fontsize,rotation=0)
    plt.xlabel('Lattice constant error',fontsize=fontsize)
    #plt.ylim(-0.4,0.2)
    plt.savefig('hf_schNET.png',dpi=150)
    plt.show()

    plt.close()

scatter(df_plot)

