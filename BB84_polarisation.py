import random
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk

app = tk.Tk()
app.title("QKD BB84 Pol. App")
#app.geometry("1000x400")

#Top Level Hiarchy
ctrlFrame = tk.Frame(app)
statusFrame = tk.Frame(app)
authorFrame = tk.Frame(app)
authorFrame.pack(side='bottom')
ctrlFrame.pack(side='left',anchor='nw')
statusFrame.pack(side='right',anchor='nw')

tk.Label(authorFrame,text=
"Developped by, Pankaj Kumar Saini | PH22M013 |"
" Department of Physics | IIT Tirupati").pack()


########################
# Control Pannel
########################
ctrlFrameHeading = tk.Frame(ctrlFrame)
ctrlLabel = tk.Label(ctrlFrameHeading,text=
                     "Control Pannel") #Control Pannel Heading Label
# Alice Button Pannel
ctrlFrame_alice_bob = tk.Frame(ctrlFrame)
basisAlice_var = tk.StringVar(ctrlFrame_alice_bob,"R")
basisLabel_alice = tk.Label(ctrlFrame_alice_bob,text="Alice's Basis: ")
basisBtn0_alice = tk.Radiobutton(ctrlFrame_alice_bob,text="0",
                                  variable=basisAlice_var, value="0")
basisBtn45_alice = tk.Radiobutton(ctrlFrame_alice_bob,text="45",
                                   variable=basisAlice_var, value="45")
basisBtn90_alice = tk.Radiobutton(ctrlFrame_alice_bob,text="90",
                                   variable=basisAlice_var, value="90")
basisBtn135_alice = tk.Radiobutton(ctrlFrame_alice_bob,text="135",
                                    variable=basisAlice_var, value="135")
basisBtnR_alice = tk.Radiobutton(ctrlFrame_alice_bob,text="Random",
                                  variable=basisAlice_var, value="R")
# Bob Button Pannel
basisBob_var = tk.StringVar(ctrlFrame_alice_bob,"R")
basisLabel_bob = tk.Label(ctrlFrame_alice_bob,text="Bob's Basis: ")
basisBtnH_V_O_bob = tk.Radiobutton(ctrlFrame_alice_bob,text="H_V_O",
                                    variable=basisBob_var, value="H_V_O")
basisBtnD_O_bob = tk.Radiobutton(ctrlFrame_alice_bob,text="D_O",
                                  variable=basisBob_var, value="D_O")
basisBtnR_bob = tk.Radiobutton(ctrlFrame_alice_bob,text="Random(H_V & D)",
                                variable=basisBob_var, value="R")
# Evesdropper Button Pannel
ctrlFrame_eve = tk.Frame(ctrlFrame)
basisEve_var = tk.StringVar(ctrlFrame_eve,False)
basisLabel_eve = tk.Label(ctrlFrame_eve,text="Evesdropper: ")
basisBtn_eve = tk.Checkbutton(ctrlFrame_eve,text="Present",
                               variable=basisEve_var)
# Simulaiton Controller Button Pannel
ctrlFrame_sim_ctrl = tk.Frame(ctrlFrame)
simCtrl = tk.StringVar(ctrlFrame_sim_ctrl,"single")
fastfwdN_var = tk.StringVar(ctrlFrame_sim_ctrl,10)
simLabel = tk.Label(ctrlFrame_sim_ctrl,text="Simulation Controller")
simBtn_single = tk.Button(ctrlFrame_sim_ctrl,text="Single Pair",
                          command=lambda:simulate('single'))
simBtn_continous = tk.Button(ctrlFrame_sim_ctrl,text="Continous",
                             command=lambda:simulate('continous'))
simBtn_fastfwd = tk.Button(ctrlFrame_sim_ctrl,text="Fast Forward",
                           command=lambda:simulate('fast_fwd'))
simBtn_fastfws_N = tk.Entry(ctrlFrame_sim_ctrl,text="N",
                            textvariable=fastfwdN_var)
clearBtn = tk.Button(ctrlFrame_sim_ctrl,text="Clear",
                     command=lambda:clearTable())
# Control Pannel Layout
ctrlFrameHeading.grid(row=0,column=0,sticky="")      ## Control Pannel Heading Frame
ctrlLabel.grid(row=0,column=0,sticky="",pady = 2)    ## Control Pannel Heading Label
ctrlFrame_alice_bob.grid(row=1,column=0,sticky="w")  ## Alice_Bob Button Pannel Frame
basisLabel_alice.grid(row=0,column=0,pady = 2)       ##
basisBtn0_alice.grid(row=0,column=1,pady = 2)        ##
basisBtn45_alice.grid(row=0,column=2,pady = 2)       ##
basisBtn90_alice.grid(row=0,column=3,pady = 2)       ##
basisBtn135_alice.grid(row=0,column=4,pady = 2)      ##
basisBtnR_alice.grid(row=0,column=5,pady = 2)        ##
basisLabel_bob.grid(row=1,column=0,pady = 2)         ##
basisBtnH_V_O_bob.grid(row=1,column=1,pady = 2)      ##
basisBtnD_O_bob.grid(row=1,column=2,pady = 2)        ##
basisBtnR_bob.grid(row=1,column=3,pady = 2)          ##
ctrlFrame_eve.grid(row=2,column=0,sticky="w")        ## Evesdropper Pannel Frame
basisLabel_eve.grid(row=0,column=0,pady=2)           ##
basisBtn_eve.grid(row=0,column=1)                    ##
ctrlFrame_sim_ctrl.grid(row=3,column=0,sticky="w")   ## Simulaiton Controller Frame
simLabel.grid(row=0,column=0)                        ##
simBtn_single.grid(row=0,column=1)                   ##
simBtn_continous.grid(row=1,column=1)                ##
simBtn_fastfwd.grid(row=2,column=1)                  ##
simBtn_fastfws_N.grid(row=2,column=2)                ##
clearBtn.grid(row=3,column=1)                        ## Clear Button Position



############################
# Status Frame
###########################
statusFrame_canvas = tk.Canvas(statusFrame)

statusFrame_msg = tk.Frame(statusFrame)

# Status Table
statusFrame_table = tk.Frame(statusFrame)
statusTable_scroll = tk.Scrollbar(statusFrame_table,
                                  orient='vertical')
statusTable = ttk.Treeview(statusFrame_table,
                           yscrollcommand=statusTable_scroll.set,
                           show='headings')
statusTable_scroll.config(command=statusTable.yview)

statusTable['columns'] = (0,1,2,3)
statusTable.column(0,width=60,anchor='center')
statusTable.column(1,width=150,anchor='w')
statusTable.column(2,width=150,anchor='w')
statusTable.column(3,width=150,anchor='w')

statusTable.heading(0,text='QBit')
statusTable.heading(1,text='Alice')
statusTable.heading(2,text='Evesdropper')
statusTable.heading(3,text='Bob')

# Key View
keyFrame = tk.Frame(statusFrame)
keyTable_scroll = tk.Scrollbar(keyFrame,
                               orient='vertical')
keyTable = ttk.Treeview(keyFrame,selectmode='browse',
                        show='headings',
                        yscrollcommand=keyTable_scroll.set)
keyTable_scroll.config(command=keyTable.yview)

keyTable['columns'] = (0)
keyTable.heading(0,text="Key")
keyTable.column(0,width=50)

key_len = 0
err_len = 0
err_percent = 0

# Error
statusFrame_err = tk.Frame(statusFrame)
errPercentLabel = tk.Label(statusFrame_err,
                           text="Evesdropper: Undetermined")


# Status Layout
statusFrame_table.grid(row=1,column=0)
keyFrame.grid(row=1,column=1)
statusFrame_err.grid(row=2,column=0)
statusTable_scroll.pack(side='right', fill='y')
keyTable_scroll.pack(side='right',fill='y')
statusTable.pack()
keyTable.pack()
errPercentLabel.pack()


# App Functions

# state zeros and one
basis = {}
basis['0'] = np.array([1,0])   #  written in the form  of zeros   ## we take it as 1
basis['45'] = np.array([1,1])  #  written in the foem of zeros    ## we take it as 2
basis['90'] = np.array([0,1])  #  written in the form of one's   ## we take it as 3
basis['135'] = np.array([1,-1]) #  written in the form of one's  ## we take it as 4
# bit=np.array([[[1],[0]],
#             [[0],[1]]]) 


def qbitMeas(alice_basis,bob_basis,isEvePresent):

    if(alice_basis=="R"):
        alice_basis = random.choice(["0","45","90","135"])
    else:
        alice_basis = alice_basis

    if(bob_basis=="R"):
        bob_basis = random.choice(["H_V_O","D_O"])
    else:
        bob_basis = bob_basis

    eve_basis = random.choice(["H_V_O","D_O"])


    alice_meas = alice_basis
    # Bob's Meas
    if((alice_basis=="0" or alice_basis=="90") and (bob_basis=="H_V_O")):
        bob_meas = alice_basis
    elif((alice_basis=="45" or alice_basis=="135") and (bob_basis=="D_O")):
        bob_meas = alice_basis
    elif((alice_basis=="0" or alice_basis=="90") and (bob_basis=="D_O")):
        bob_meas = random.choice(["45","135"])
    elif((alice_basis=="45" or alice_basis=="135") and (bob_basis=="H_V_O")):
        bob_meas = random.choice(["0","90"])
    else:
        bob_meas = "--"

    #Eve's Meas (if eve is present)
    if((alice_basis=="0" or alice_basis=="90") and (eve_basis=="H_V_O")):
        eve_meas = alice_basis
    elif((alice_basis=="45" or alice_basis=="135") and (eve_basis=="D_O")):
        eve_meas = alice_basis
    elif((alice_basis=="0" or alice_basis=="90") and (eve_basis=="D_O")):
        eve_meas = random.choice(["45","135"])
    elif((alice_basis=="45" or alice_basis=="135") and (eve_basis=="H_V_O")):
        eve_meas = random.choice(["0","90"])
    else:
        eve_meas = "--"


    if(isEvePresent=="1"):
        if((eve_meas=="0" or eve_meas=="90") and (bob_basis=="H_V_O")):
            bob_meas = eve_meas
        elif((eve_meas=="45" or eve_meas=="135") and (bob_basis=="D_O")):
            bob_meas = eve_meas
        elif((eve_meas=="0" or eve_meas=="90") and (bob_basis=="D_O")):
            bob_meas = random.choice(["45","135"])
        elif((eve_meas=="45" or eve_meas=="135") and (bob_basis=="H_V_O")):
            bob_meas = random.choice(["0","90"])
        else:
            bob_meas = "--"
    else:
        eve_basis="--"
        eve_meas = "--"
        bob_meas = bob_meas

    return([0,alice_basis,alice_meas,eve_basis,eve_meas,bob_basis,bob_meas]) 

def pushTable(data): 
# Data Template - [Qbit,alice_basis,alice_meas,eve_basis,eve_meas,bob_basis,bob_meas]
    global err_len, key_len, err_percent
    colData = ("--",
               'Basis: ' + str(data[1]) + '    Data: ' + str(data[2]),
               'Basis: ' + str(data[3]) + '    Data: ' + str(data[4]),
               'Basis: ' + str(data[5]) + '    Data: ' + str(data[6]))
    statusTable.insert(parent='',index='end',values=colData)


    if((data[1]=="0" or data[1]=="90") and data[5]=="H_V_O"):
        pushKey(data[6])
    elif((data[1]=="45" or data[1]=="135") and data[5]=="D_O"):
        pushKey(data[6])
    else:
        #pushKey("--")
        True
    
    if(data[3] != "--" and ((((data[1] == "0" or data[1] == "90") and  
                              data[5] == "H_V_O") or ((data[1] == "45" or 
                                                       data[1] == "135") and 
                                                       data[5] == "D_O")) and 
                                                       (data[2] != data[6]))):
        errPercentLabel.config(text="Evesdropper: Present")
    else:
        True
    

def clearTable():
    statusTable.delete(*statusTable.get_children())
    keyTable.delete(*keyTable.get_children())
    errPercentLabel.config(text="Evesdropper: Undetermined")
    global err_len, key_len
    err_len = 0
    key_len = 0

def pushKey(key):
    global key_len
    keyTable.insert(parent='',index='end',value=key)
    key_len = key_len+1


def simulate(sim_type):
    basisAlice  = basisAlice_var.get()
    basisBob    = basisBob_var.get()
    ifEve = basisEve_var.get()
    fastfwdN = int(fastfwdN_var.get())

    if(sim_type=='continous'):
        i=0
        while(i<1000):
            pushTable(qbitMeas(basisAlice,basisBob,ifEve))
            i=i+1
        pushTable(qbitMeas(basisAlice,basisBob,ifEve))
        return 0
    
    elif(sim_type=='fast_fwd'):

        i=0
        while(i<fastfwdN):
            pushTable(qbitMeas(basisAlice,basisBob,ifEve))
            i=i+1
        return 0
    
    else: # For single
        pushTable(qbitMeas(basisAlice,basisBob,ifEve))
        return 0

app.mainloop()