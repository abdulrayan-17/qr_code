import tkinter as tk
import qrcode

def generate_qr_code():
    url = url_entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")
    result_label.config(text="QR Code generated successfully!")

# Create the main application window
app = tk.Tk()
app.title("QR Code Generator")

# Create and configure GUI elements
label = tk.Label(app, text="Enter URL:")
label.pack(pady=10)
url_entry = tk.Entry(app)
url_entry.pack(pady=10)
generate_button = tk.Button(app, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()
result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Start the GUI application
app.mainloop()
