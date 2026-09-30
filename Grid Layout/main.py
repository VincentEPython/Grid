import tkinter as tk

window = tk.Tk()

name_label = tk.Label(window,text= "Name")
name_label.grid(row=1, column=1)
 
name_entry = tk.Entry(window)
name_entry.grid(row=1,column= 2)

email_label = tk.Label(window,text= "Email")
email_label.grid(row=2, column=1)

email_entry = tk.Entry(window)
email_entry.grid(row=2,column= 2)

phone_label = tk.Label(window, text = "Phone")
phone_label.grid(row=3, column= 1)

phone_entry = tk.Entry(window)
phone_entry.grid(row=3,column=2)

savecontact_button = tk.Button(window, text = "Save Contact",width=22)
savecontact_button.grid(row=4, column=1,columnspan=2)






window.mainloop()
