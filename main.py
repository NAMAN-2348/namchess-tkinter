from tkinter import *
chs=Tk()
chs.geometry('600x600')
chs.title("NAMCHESS")
bggl=Label(chs,text=' '*18+"\n"+' '*18,font=("arial",200),bg='sky blue')
bggl.place(x=0,y=0)
chsl=[]
for i in range(0,8):
    chls=[]
    for j in range(0,8):
        chl='chlb'+str(i)+str(j)
        chls.append(chl)
    chsl.append(chls)

pcl=[]
pclt=[]
for i in range(0,8):
    pcls=[]
    pclst=[]
    for j in range(0,8):
        if i==0 and (j==0 or j==7):
            pcls.append('♜')
            pclst.append('br')
        elif i==0 and (j==1 or j==6):
            pcls.append('♞')
            pclst.append('bn')
        elif i==0 and (j==2 or j==5):
            pcls.append('♝')
            pclst.append('bb')
        elif i==0 and (j==3):
            pcls.append('♛')
            pclst.append('bq')
        elif i==0 and (j==4):
            pcls.append('♚')
            pclst.append('bk')
        elif i==1:
            pcls.append('♟')
            pclst.append('bp')
        elif i==7 and (j==0 or j==7):
            pcls.append('♖')
            pclst.append('wr')
        elif i==7 and (j==1 or j==6):
            pcls.append('♘')
            pclst.append('wn')
        elif i==7 and (j==2 or j==5):
            pcls.append('♗')
            pclst.append('wb')
        elif i==7 and (j==3):
            pcls.append('♕')
            pclst.append('wq')
        elif i==7 and (j==4):
            pcls.append('♔')
            pclst.append('wk')
        elif i==6:
            pcls.append('♙')
            pclst.append('wp')
        else:
            pcls.append(' '*7+'\n'+' '*7)
            pclst.append('s')
    pcl.append(pcls)
    pclt.append(pclst)
#snow ♔♕♖♗♘♙
#black ♚♛♜♝♞♟
co=cob=0
pcin=[]
def clrcd(pcin):
    for i in range(0,8):
        for j in range(0,8):
            chsl[i][j].config(bg='green')
            if i%2==0:
                if j%2==0:
                    chsl[i][j].config(bg='snow')
            else:
                if j%2==1:
                    chsl[i][j].config(bg='snow')
            if (i==pcin[1][0] and j==pcin[1][1]):
                chsl[i][j].config(bg='lime green')
            if (i==pcin[0][0] and j==pcin[0][1]):
                chsl[i][j].config(bg='yellow green')
def pcplc(pcin):
    chsl[pcin[1][0]][pcin[1][1]].config(text=pcl[pcin[0][0]][pcin[0][1]])
    pcl[pcin[1][0]][pcin[1][1]]=pcl[pcin[0][0]][pcin[0][1]]
    pclt[pcin[1][0]][pcin[1][1]]=pclt[pcin[0][0]][pcin[0][1]]
    chsl[pcin[0][0]][pcin[0][1]].config(text=' '*7+'\n'+' '*7)
    pcl[pcin[0][0]][pcin[0][1]]=' '*7+'\n'+' '*7
    pclt[pcin[0][0]][pcin[0][1]]='s'
def pcmove(x):
    global pcin,co,cob
    co+=1
    pcin.append(x)
    if (co%2==0 and ([pcin[1][0],pcin[1][1]]!=[pcin[0][0],pcin[0][1]]) and pclt[pcin[1][0]][pcin[1][1]][0]!=pclt[pcin[0][0]][pcin[0][1]][0] and (pclt[pcin[0][0]][pcin[0][1]]!='s')):
        if (len(pclt[pcin[1][0]][pcin[1][1]])==2):
            if (pclt[pcin[1][0]][pcin[1][1]][1]=='k'):
                pcin=[]
                return None
        if cob%2==0:
            if pclt[pcin[0][0]][pcin[0][1]][0]=='b':
                pcin=[]
                return None
        else:
            if pclt[pcin[0][0]][pcin[0][1]][0]=='w':
                pcin=[]
                return None
        if pclt[pcin[0][0]][pcin[0][1]][1]=='r':
            pos=[]
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=0):
                i-=1
                j-=0
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (j!=7):
                i-=0
                j+=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (j!=0):
                i+=0
                j-=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=7):
                i+=1
                j-=0
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            if [pcin[1][0],pcin[1][1]] in pos:
                pcplc(pcin)
                cob+=1
                clrcd(pcin)
        elif pclt[pcin[0][0]][pcin[0][1]][1]=='n':
            pos=[[pcin[0][0]-2,pcin[0][1]-1],[pcin[0][0]-2,pcin[0][1]+1],[pcin[0][0]-1,pcin[0][1]+2],[pcin[0][0]+1,pcin[0][1]+2],[pcin[0][0]+2,pcin[0][1]+1],[pcin[0][0]+2,pcin[0][1]-1],[pcin[0][0]+1,pcin[0][1]-2],[pcin[0][0]-1,pcin[0][1]-2]]
            if [pcin[1][0],pcin[1][1]] in pos:
                pcplc(pcin)
                cob+=1
                clrcd(pcin)
        elif pclt[pcin[0][0]][pcin[0][1]][1]=='p':
            # Pawns move forward into empty squares and capture diagonally.
            # On the starting rank, a two-square move is permitted only when
            # both the intermediate and destination squares are empty.
            origin_row, origin_col = pcin[0]
            dest_row, dest_col = pcin[1]
            pawn = pclt[origin_row][origin_col]
            destination = pclt[dest_row][dest_col]
            direction = -1 if pawn[0] == 'w' else 1
            starting_row = 6 if pawn[0] == 'w' else 1
            row_delta = dest_row - origin_row
            col_delta = dest_col - origin_col
            legal_pawn_move = False

            if col_delta == 0 and destination == 's':
                if row_delta == direction:
                    legal_pawn_move = True
                elif (
                    origin_row == starting_row
                    and row_delta == 2 * direction
                    and pclt[origin_row + direction][origin_col] == 's'
                ):
                    legal_pawn_move = True
            elif (
                abs(col_delta) == 1
                and row_delta == direction
                and destination != 's'
                and destination[0] != pawn[0]
            ):
                legal_pawn_move = True

            if legal_pawn_move:
                pcplc(pcin)
                cob += 1
                clrcd(pcin)
        elif pclt[pcin[0][0]][pcin[0][1]][1]=='k':
            pos=[[pcin[0][0]+1,pcin[0][1]],[pcin[0][0]+1,pcin[0][1]+1],[pcin[0][0],pcin[0][1]+1],[pcin[0][0]-1,pcin[0][1]+1],[pcin[0][0]-1,pcin[0][1]],[pcin[0][0]-1,pcin[0][1]-1],[pcin[0][0],pcin[0][1]-1],[pcin[0][0]+1,pcin[0][1]-1]]
            if [pcin[1][0],pcin[1][1]] in pos:
                pcplc(pcin)
                cob+=1
                clrcd(pcin)
        elif pclt[pcin[0][0]][pcin[0][1]][1]=='b':
            pos=[]
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=0 and j!=0):
                i-=1
                j-=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=0 and j!=7):
                i-=1
                j+=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=7 and j!=0):
                i+=1
                j-=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=7 and j!=7):
                i+=1
                j+=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            if [pcin[1][0],pcin[1][1]] in pos:
                pcplc(pcin)
                cob+=1
                clrcd(pcin)
        elif pclt[pcin[0][0]][pcin[0][1]][1]=='q':
            pos=[]
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=0 and j!=0):
                i-=1
                j-=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=0 and j!=7):
                i-=1
                j+=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=7 and j!=0):
                i+=1
                j-=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=7 and j!=7):
                i+=1
                j+=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=0):
                i-=1
                j-=0
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (j!=7):
                i-=0
                j+=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (j!=0):
                i+=0
                j-=1
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            i=pcin[0][0]
            j=pcin[0][1]
            while (i!=7):
                i+=1
                j+=0
                pos.append([i,j])
                if pclt[i][j]!='s':
                    break
            if [pcin[1][0],pcin[1][1]] in pos:
                pcplc(pcin)
                cob+=1
                clrcd(pcin)
    if co%2==0:
        pcin=[]
def ind00():
    x=[0,0]
    pcmove(x)
def ind01():
    x=[0,1]
    pcmove(x)
def ind02():
    x=[0,2]
    pcmove(x)
def ind03():
    x=[0,3]
    pcmove(x)
def ind04():
    x=[0,4]
    pcmove(x)
def ind05():
    x=[0,5]
    pcmove(x)
def ind06():
    x=[0,6]
    pcmove(x)
def ind07():
    x=[0,7]
    pcmove(x)
def ind10():
    x=[1,0]
    pcmove(x)
def ind11():
    x=[1,1]
    pcmove(x)
def ind12():
    x=[1,2]
    pcmove(x)
def ind13():
    x=[1,3]
    pcmove(x)
def ind14():
    x=[1,4]
    pcmove(x)
def ind15():
    x=[1,5]
    pcmove(x)
def ind16():
    x=[1,6]
    pcmove(x)
def ind17():
    x=[1,7]
    pcmove(x)
def ind20():
    x=[2,0]
    pcmove(x)
def ind21():
    x=[2,1]
    pcmove(x)
def ind22():
    x=[2,2]
    pcmove(x)
def ind23():
    x=[2,3]
    pcmove(x)
def ind24():
    x=[2,4]
    pcmove(x)
def ind25():
    x=[2,5]
    pcmove(x)
def ind26():
    x=[2,6]
    pcmove(x)
def ind27():
    x=[2,7]
    pcmove(x)
def ind30():
    x=[3,0]
    pcmove(x)
def ind31():
    x=[3,1]
    pcmove(x)
def ind32():
    x=[3,2]
    pcmove(x)
def ind33():
    x=[3,3]
    pcmove(x)
def ind34():
    x=[3,4]
    pcmove(x)
def ind35():
    x=[3,5]
    pcmove(x)
def ind36():
    x=[3,6]
    pcmove(x)
def ind37():
    x=[3,7]
    pcmove(x)
def ind40():
    x=[4,0]
    pcmove(x)
def ind41():
    x=[4,1]
    pcmove(x)
def ind42():
    x=[4,2]
    pcmove(x)
def ind43():
    x=[4,3]
    pcmove(x)
def ind44():
    x=[4,4]
    pcmove(x)
def ind45():
    x=[4,5]
    pcmove(x)
def ind46():
    x=[4,6]
    pcmove(x)
def ind47():
    x=[4,7]
    pcmove(x)
def ind50():
    x=[5,0]
    pcmove(x)
def ind51():
    x=[5,1]
    pcmove(x)
def ind52():
    x=[5,2]
    pcmove(x)
def ind53():
    x=[5,3]
    pcmove(x)
def ind54():
    x=[5,4]
    pcmove(x)
def ind55():
    x=[5,5]
    pcmove(x)
def ind56():
    x=[5,6]
    pcmove(x)
def ind57():
    x=[5,7]
    pcmove(x)
def ind60():
    x=[6,0]
    pcmove(x)
def ind61():
    x=[6,1]
    pcmove(x)
def ind62():
    x=[6,2]
    pcmove(x)
def ind63():
    x=[6,3]
    pcmove(x)
def ind64():
    x=[6,4]
    pcmove(x)
def ind65():
    x=[6,5]
    pcmove(x)
def ind66():
    x=[6,6]
    pcmove(x)
def ind67():
    x=[6,7]
    pcmove(x)
def ind70():
    x=[7,0]
    pcmove(x)
def ind71():
    x=[7,1]
    pcmove(x)
def ind72():
    x=[7,2]
    pcmove(x)
def ind73():
    x=[7,3]
    pcmove(x)
def ind74():
    x=[7,4]
    pcmove(x)
def ind75():
    x=[7,5]
    pcmove(x)
def ind76():
    x=[7,6]
    pcmove(x)
def ind77():
    x=[7,7]
    pcmove(x)
butom=[[ind00,ind01,ind02,ind03,ind04,ind05,ind06,ind07],[ind10,ind11,ind12,ind13,ind14,ind15,ind16,ind17],[ind20,ind21,ind22,ind23,ind24,ind25,ind26,ind27],[ind30,ind31,ind32,ind33,ind34,ind35,ind36,ind37],[ind40,ind41,ind42,ind43,ind44,ind45,ind46,ind47],[ind50,ind51,ind52,ind53,ind54,ind55,ind56,ind57],[ind60,ind61,ind62,ind63,ind64,ind65,ind66,ind67],[ind70,ind71,ind72,ind73,ind74,ind75,ind76,ind77]]
for i in range(0,8):
    for j in range(0,8):
        chsl[i][j]=Button(chs,text=pcl[i][j],font=("Segoe UI Symbol",29),bg='green',command=butom[i][j])
        chsl[i][j].place(x=20+70*j,y=40+60*i)
        if i%2==0:
            if j%2==0:
                chsl[i][j].config(bg='snow')
        else:
            if j%2==1:
                chsl[i][j].config(bg='snow')
bag2=Label(chs,text=' ',font=('arial',400),bg='sky blue')
bag2.place(x=580,y=0)
bag3=Label(chs,text=' '*18,font=('arial',400),bg='sky blue')
bag3.place(x=0,y=520)
chs.mainloop()