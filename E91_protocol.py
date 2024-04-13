import random
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk

app = tk.Tk()
app.title("QKD E91 App")
#app.geometry("1000x400")

#Top Level Hiarchy
ctrlFrame = tk.Frame(app)
statusFrame = tk.Frame(app)
authorFrame = tk.Frame(app)
authorFrame.pack(side='bottom')
ctrlFrame.pack(side='left',anchor='nw')
statusFrame.pack(side='right',anchor='nw')

tk.Label(authorFrame,text="Developped by, Pankaj Saini | PH22M013 | Department of Physics | Indian Institute of Technology Tirupati").pack()


########################
# Control Pannel
########################
ctrlFrameHeading = tk.Frame(ctrlFrame)
ctrlLabel = tk.Label(ctrlFrameHeading,text="Control Pannel")    #Control Pannel Heading Label

# Alice Button Pannel
ctrlFrame_alice_bob = tk.Frame(ctrlFrame)
basisAlice_var = tk.StringVar(ctrlFrame_alice_bob,"X")
basisLabel_alice = tk.Label(ctrlFrame_alice_bob,text="Alice's Basis: ")
basisBtnX_alice = tk.Radiobutton(ctrlFrame_alice_bob,text="X", variable=basisAlice_var, value="X")
basisBtnZ_alice = tk.Radiobutton(ctrlFrame_alice_bob,text="Z", variable=basisAlice_var, value="Z")
basisBtnR_alice = tk.Radiobutton(ctrlFrame_alice_bob,text="Random", variable=basisAlice_var, value="R")

# Bob Button Pannel
basisBob_var = tk.StringVar(ctrlFrame_alice_bob,"X")
basisLabel_bob = tk.Label(ctrlFrame_alice_bob,text="Bob's Basis: ")
basisBtnX_bob = tk.Radiobutton(ctrlFrame_alice_bob,text="X", variable=basisBob_var, value="X")
basisBtnZ_bob = tk.Radiobutton(ctrlFrame_alice_bob,text="Z", variable=basisBob_var, value="Z")
basisBtnR_bob = tk.Radiobutton(ctrlFrame_alice_bob,text="Random", variable=basisBob_var, value="R")

# Evesdropper Button Pannel
ctrlFrame_eve = tk.Frame(ctrlFrame)
basisEve_var = tk.StringVar(ctrlFrame_eve,False)
basisLabel_eve = tk.Label(ctrlFrame_eve,text="Evesdropper: ")
basisBtn_eve = tk.Checkbutton(ctrlFrame_eve,text="Present", variable=basisEve_var)
# Simulaiton Controller Button Pannel
ctrlFrame_sim_ctrl = tk.Frame(ctrlFrame)
simCtrl = tk.StringVar(ctrlFrame_sim_ctrl,"single")
fastfwdN_var = tk.StringVar(ctrlFrame_sim_ctrl,10)
simLabel = tk.Label(ctrlFrame_sim_ctrl,text="Simulation Controller")
simBtn_single = tk.Button(ctrlFrame_sim_ctrl,text="Single Pair",command=lambda:simulate('single'))
simBtn_continous = tk.Button(ctrlFrame_sim_ctrl,text="continous",command=lambda:simulate('continous'))
simBtn_fastfwd = tk.Button(ctrlFrame_sim_ctrl,text="Fast Forward",command=lambda:simulate('fast_fwd'))
simBtn_fastfws_N = tk.Entry(ctrlFrame_sim_ctrl,text="N",textvariable=fastfwdN_var)
clearBtn = tk.Button(ctrlFrame_sim_ctrl,text="Clear",command=lambda:clearTable())

# Control Pannel Layout
ctrlFrameHeading.grid(row=0,column=0,sticky="")         # Control Pannel Heading Frame
ctrlLabel.grid(row=0,column=0,sticky="",pady = 2)       ## Control Pannel Heading Label
ctrlFrame_alice_bob.grid(row=1,column=0,sticky="w")     # Alice_Bob Button Pannel Frame
basisLabel_alice.grid(row=0,column=0,pady = 2)              ##
basisBtnX_alice.grid(row=0,column=1,pady = 2)               ##
basisBtnZ_alice.grid(row=0,column=2,pady = 2)               ##
basisBtnR_alice.grid(row=0,column=3,pady = 2)               ##
basisLabel_bob.grid(row=1,column=0,pady = 2)                ##
basisBtnX_bob.grid(row=1,column=1,pady = 2)                 ##
basisBtnZ_bob.grid(row=1,column=2,pady = 2)                 ##
basisBtnR_bob.grid(row=1,column=3,pady = 2)                 ##
ctrlFrame_eve.grid(row=2,column=0,sticky="w")           # Evesdropper Pannel Frame
basisLabel_eve.grid(row=0,column=0,pady=2)                  ##
basisBtn_eve.grid(row=0,column=1)                           ##
ctrlFrame_sim_ctrl.grid(row=3,column=0,sticky="w")      # Simulaiton Controller Frame
simLabel.grid(row=0,column=0)                               ##
simBtn_single.grid(row=0,column=1)                          ##
simBtn_continous.grid(row=1,column=1)                       ##
simBtn_fastfwd.grid(row=2,column=1)                         ##
simBtn_fastfws_N.grid(row=2,column=2)                       ##
clearBtn.grid(row=3,column=1)                               ## Clear Button Position



############################
# Status Frame
###########################
statusFrame_canvas = tk.Canvas(statusFrame)

statusFrame_msg = tk.Frame(statusFrame)

# Status Table
statusFrame_table = tk.Frame(statusFrame)
statusTable_scroll = tk.Scrollbar(statusFrame_table,orient='vertical')
statusTable = ttk.Treeview(statusFrame_table,yscrollcommand=statusTable_scroll.set,show='headings')
statusTable_scroll.config(command=statusTable.yview)

statusTable['columns'] = (0,1,2,3)
statusTable.column(0,width=0,anchor='center')
statusTable.column(1,width=150,anchor='w')
statusTable.column(2,width=150,anchor='w')
statusTable.column(3,width=150,anchor='w')

# statusTable.heading(0,text='QBit')
statusTable.heading(1,text='Alice')
statusTable.heading(2,text='Evesdropper')
statusTable.heading(3,text='Bob')

# Key View
keyFrame = tk.Frame(statusFrame)
keyTable_scroll = tk.Scrollbar(keyFrame,orient='vertical')
keyTable = ttk.Treeview(keyFrame,selectmode='browse',show='headings',yscrollcommand=keyTable_scroll.set)
keyTable_scroll.config(command=keyTable.yview)

keyTable['columns'] = (0)
keyTable.heading(0,text="Key")
keyTable.column(0,width=50)

key_len = 0
err_len = 0
err_percent = 0

# Error
statusFrame_err = tk.Frame(statusFrame)
errPercentLabel = tk.Label(statusFrame_err,text="p(Error)=")


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
basis['X'] = np.array([[0,1],[1,0]])   # Pauli-X matrix
basis['Z'] = np.array([[1,0],[0,-1]])  # Pauli-Z matrix
bit=np.array([[[1],[0]],
            [[0],[1]]]) 


def qbitMeas(alice_basis,bob_basis,isEvePresent):
    bitID = random.choice([0,1])
    aliceBitID = bitID #IF aliceBit = 0 -> bobBit = 1 || aliceBit = 1 -> bobBit = 0
    bobBitID = 1-bitID

    eve_basis = random.choice(['X','Z'])
    if(alice_basis=="R"):
        alice_basis = random.choice(['X','Z'])
    else:
        alice_basis = alice_basis
    if(bob_basis=="R"):
        bob_basis = random.choice(['X','Z'])
    else:
        bob_basis = bob_basis

    alice_meas = np.matmul(basis[alice_basis],bit[aliceBitID])
    eve_meas = np.matmul(basis[eve_basis],bit[bobBitID])

    if((eve_meas==[[0],[-1]]).all()):
        eve_meas = np.array([[0],[1]])
    elif((eve_meas==[[-1],[0]]).all()):
        eve_meas = np.array([[1],[0]])
    else:
         eve_meas = eve_meas

    if(isEvePresent=="1"):
        bob_meas = np.matmul(basis[bob_basis],eve_meas)
    else:
        bob_meas = np.matmul(basis[bob_basis],bit[bobBitID])
        eve_meas = np.array([0,0])
        eve_basis = "NA"

    if((alice_meas==bit[0]).all()):
        alice_meas = 0
    else:
        alice_meas = 1

    if((bob_meas==bit[0]).all()):
        bob_meas = 0
    else:
        bob_meas = 1

    if((eve_meas==bit[0]).all()):
        eve_meas = 0
    elif((eve_meas==bit[1]).all() or (eve_meas==[[0],[-1]]).all()):
        eve_meas = 1
    else:
        eve_meas = "NA"

    return([bitID,alice_basis,alice_meas,eve_basis,eve_meas,bob_basis,bob_meas]) 

def pushTable(data): # Data Template - [Qbit,alice_basis,alice_meas,eve_basis,eve_meas,bob_basis,bob_meas]
    global err_len, key_len, err_percent
    colData = ("",
               'Basis: ' + str(data[1]) + '    Data: ' + str(data[2]),
               'Basis: ' + str(data[3]) + '    Data: ' + str(data[4]),
               'Basis: ' + str(data[5]) + '    Data: ' + str(data[6]))
    statusTable.insert(parent='',index='end',values=colData)
    keyData = 1 - data[6] # If data[6] = 1, key=0 || If data[6] = 0, key = 1
    if(basisEve_var.get() == "0" and data[1] == data[5]):  # if Eve is absent, alice_basis == bob_basis
        pushKey(keyData)                                    # put bob_meas to keyTable
    elif(basisEve_var.get() == "1" and data[1] == data[5]):     # If Eve is present, alice_bais == bob_basis
        pushKey(keyData)
        if(data[0] != keyData): # if qubit sent to alice is not equal to bob_decoded data
            err_len = err_len + 1

    err_percent = err_len/key_len*100
    errPercentLabel.config(text="p(Error)=" + str(np.floor(err_percent*100)/100) + "%")
    
    
    

def clearTable():
    statusTable.delete(*statusTable.get_children())
    keyTable.delete(*keyTable.get_children())
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