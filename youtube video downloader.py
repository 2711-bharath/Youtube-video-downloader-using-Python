from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import  *

file_size = 0

# This gets called for updating percentage
def progress(stream,chunk,file_handle,remaining=None):
    #gets the percentage of file downloaded
    file_downloaded=(file_size-file_handle)
    per=(file_downloaded / file_size) * 100
    dBtn.config(text="{:00.0f} % downloaded".format(per))


def startDownload():
    global file_size
    try:
        url = urlFeild.get()
        print(url)
        # changing button text
        dBtn.config(text="please wait...")
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return
        ob = YouTube(url,on_progress_callback=progress)
        # strms = ob.streams.all()
        # for s in strms:
        #     print(s)

        strm = ob.streams.first()
        file_size = strm.filesize
        # print(strm)
        print(strm.filesize)
        # print(strm.title)
        # print(ob.description)
        # print(ob.views)
        # print(ob.title)

        strm.download(output_path=path_to_save_video)
        print("done...")
        dBtn.config(text="start download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished","Downloaded Successfully")
        urlFeild.delete(0,END)
    except Exception as e:
        print(e)
        print("Error !!")

def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()

#Making GUI

main = Tk()

# setting the title
main.title("Youtube Downloader")

# setting an icon
main.iconbitmap("youtube.ico")

main.geometry("400x500")

#heading icon

file = PhotoImage(file="youtube.png")
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP)

# url textfeild
urlFeild = Entry(main,font=("verdana",16),justify=CENTER)
urlFeild.pack(side=TOP,fill=X,padx=10,pady=10)

# download button
dBtn = Button(main,text="start download",font=("verdana",16),relief='ridge',command=startDownloadThread)
dBtn.pack(side=TOP,pady=10)

main.mainloop()