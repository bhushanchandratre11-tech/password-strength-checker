import re
import tkinter as tk
from tkinter import messagebox

# common weak passward
weak=[
    "1234567890",
    "abc123",
    "987654321",
    "password"
]

# function to check password strength
def password_strength_check():
    password = password_entry.get()

    score = 0
    suggestion = []

# length check
    if len(password) >=8:
        score +=1
    else:
        suggestion.append(". password atleast contain more than 8 character")

# uppercase check
    if re.search(r"[A-Z]",password):
        score +=1
    else:
        suggestion.append(".atleast one uppercase letter is required")

# lowercase check
    if re.search(r"[a-z]",password):
        score +=1
    else:
        suggestion.append(".atleast one lowercase letter is required")

# special character 
    if re.search(r"[!@#$%^&*~]",password):
        score +=1
    else:
        suggestion.append(".atleast one special character is required")

# number check
    if re.search(r"\d",password):
        score +=1
    else:
        suggestion.append(".atleast one number is reqired")

# weak password
    if password.lower() in weak:
        suggestion.append(".common password detected")

# strength levels check
    if score==5:
        strength="very storng"
        color="dark green"
    
    elif score==4:
        strength="storng"
        color="light green"
    
    elif score==3:
        strength="good"
        color="dark orange"
    
    elif score==2:
        strength="weak"
        color="light orange"
    
    else:
        strength="very weak"
        color="red"

    # Update result label
    result_label.config(
    text=f"Password Strength: {strength}",
    fg=color
)
  
# display suggestion
    suggestion_text.delete("1.0",tk.END)

    if suggestion:
        suggestion_text.insert(tk.END,"\n".join(suggestion))
    else:
        suggestion_text.insert(tk.END,"excellent password")

# password visibility
def password_visibility():
    if password_entry.cget('show')=='*':
        password_entry.config(show='')
        show_button.config(text='Hide')
    else:
        password_entry.config(show='*')
        password_entry.config(text="show")

# main window
root=tk.Tk()
root.title('password strength checker')
root.geometry('600x700')
root.config(bg="black")

# heading
heading = tk.Label( 
    root,
    bg="black",
    text="password strength checker",
    fg="white",
    font=("arial",18,"bold")
)
heading.pack(pady=15)

# password label
password_label= tk.Label(
    root,
    text="enter password",
    bg="black",
    fg="white",
    font=("arial",12)

)
password_label.pack()

# password frame
password_frame=tk.Frame(root,bg="black")
password_frame.pack(pady=10)

# password entry
password_entry=tk.Entry(
    password_frame,
    width=30,
    font=("arial",14),
    show="*"
)
password_entry.pack(side=tk.LEFT , padx=5)

# show/hide button
show_button=tk.Button(
    password_frame,
    bg="black",
    text="show",
    fg="white",
    command=password_visibility
    )
show_button.pack(side=tk.LEFT)

# check button
check_button = tk.Button(
    root,
    text="Check Strength",
    command=password_strength_check,
    font=("Arial", 12, "bold"),
    bg="#0078D7",
    fg="white",
    padx=10,
    pady=5
)
check_button.pack(pady=15)

# result label
result_label=tk.Label(
    root,
    text="" ,
    font=("arial",14,"bold"),
    bg="black"

)
result_label.pack()
# suggestion box
suggestion_text=tk.Text(
    root,
    height=8,
    width=50,
    font=("Arial", 10),
    bg="#2d2d2d",
    fg="white"
)
suggestion_text.pack(pady=15)

# run application
root.mainloop()