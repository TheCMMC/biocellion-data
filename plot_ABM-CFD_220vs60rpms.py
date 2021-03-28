import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [4.1, 3.6 ]
plt.rcParams["figure.dpi"] = 300

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE )     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE )    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE )    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE )    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE )    # legend fontsize


#parameterSets = [[1,3,5,7, 9,11,13,15,17],  # rmp = 60
#                 [2,4,6,8,10,12,14,16,18]]  # rmp = 220  

steps_doublingt = 50.0 ; # (doublingtime)/((baseline time step) * (printing frequency)  ) 
                   # (0.1) / ( 0.00002 * 100 )

parameterSets = [[5,6],
                 [7,8],
                 [9,10],
                 [11,12],
                 [13,14],
                 [15,16],
                 [17,18]]  # rmp = 6i0
colors = ['b','r']
exponents = [ '5-6','7-8', '9-10','11-12','13-14','15-16','17-18' ]
Nfigs = len(parameterSets) 
labels =  ['rpm=60','rpm=220']
run = '8'

for j in range( Nfigs ) :

    exp = str( exponents[j] ) 
    parameters = parameterSets[j]

    Nparams = len(parameters) 
    fig, ax = plt.subplots()
    for i in range(Nparams) :

        live = []
        death = []
        param = str( parameters[i] ) ;
    
        filename =  "./PLOSOne-ABM-CFD-microcarrier/output_parameter"+ param  +"_trial"+ run +".txt"
        with open(filename, 'r' ) as f :
            for line in f :
                #if 'Live Cells' in line :
                if 'Live Attached Cells' in line :
                    live.append( int( line.strip().split(':')[-1] ) )
                elif 'Removed Cells' in line :
                    death.append( int( line.strip().split(':')[-1] ) )

        Npoints = len( live )
        tsteps = [ float(t) / steps_doublingt  for t in   range( Npoints) ] ;

        if ( j == 4 ) :
            ax.plot(tsteps, live , colors[i] ,  label= labels[i] + '(live)' , linewidth=1.0 )
            ax.plot(tsteps,death , colors[i] + '--' ,  label= labels[i]+'(death)', linewidth=0.5 )
        else :
            ax.plot(tsteps, live , colors[i]  , linewidth=1.0 )
            ax.plot(tsteps,death , colors[i] + '--' ,   linewidth=0.5 )


    #ax.set_xlim([0, 1250])
    ax.set_ylim([-1, 250])
    #ax.set_yscale('log')
    plt.ylabel('Cell count', fontsize=10)
    plt.xlabel('Number of doubling times', fontsize=10)
    plt.grid()
    legend = ax.legend(loc='upper left' )
    plt.savefig("ABM-CFD_attachedcells_tresholds_"+ exp +"_run"+ run +".png", dpi=150)
