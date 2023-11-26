import tkinter as tk
from tkinter import ttk, messagebox

class DictionaryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("คำศัพท์พจนานุกรม")

        # สร้างตารางแสดงผล
        self.tree = ttk.Treeview(master, columns=("English", "Thai", "Type"), show="headings")
        self.tree.heading("English", text="คำศัพท์ภาษาอังกฤษ")
        self.tree.heading("Thai", text="คำแปลภาษาไทย")
        self.tree.heading("Type", text="ชนิดของคำ")
        self.tree.pack(pady=10)

        # เพิ่มปุ่ม
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="เพิ่มคำศัพท์", command=self.add_word)
        add_btn.grid(row=0, column=0, padx=10)

        delete_btn = tk.Button(btn_frame, text="ลบคำศัพท์", command=self.delete_word)
        delete_btn.grid(row=0, column=1, padx=10)

        # เพิ่ม Entry และปุ่มค้นหา
        search_label = tk.Label(btn_frame, text="ค้นหาคำศัพท์:")
        search_label.grid(row=0, column=2, padx=10)

        self.search_entry = tk.Entry(btn_frame, width=20)
        self.search_entry.grid(row=0, column=3, padx=10)

        search_btn = tk.Button(btn_frame, text="ค้นหา", command=self.search_word)
        search_btn.grid(row=0, column=4, padx=10)

        # ข้อมูลตัวอย่าง
        self.words = [
            {"English": "Hello", "Thai": "สวัสดี", "Type": "greeting"},
            {"English": "Computer", "Thai": "คอมพิวเตอร์", "Type": "noun"},
            # เพิ่มคำศัพท์ต่อไปได้ตามต้องการ
        ]

        # แสดงคำศัพท์ทั้งหมด
        self.show_words()

    def show_words(self):
        # ลบข้อมูลทั้งหมดในตาราง
        for record in self.tree.get_children():
            self.tree.delete(record)

        # แสดงคำศัพท์ทั้งหมดจาก self.words
        for word in self.words:
            self.tree.insert("", "end", values=(word["English"], word["Thai"], word["Type"]))

    def add_word(self):
        # สร้างหน้าต่างใหม่สำหรับเพิ่มคำศัพท์
        add_window = tk.Toplevel(self.master)
        add_window.title("เพิ่มคำศัพท์")

        # สร้าง Entry widgets สำหรับกรอกข้อมูล
        english_entry = tk.Entry(add_window, width=30)
        thai_entry = tk.Entry(add_window, width=30)
        type_entry = tk.Entry(add_window, width=30)

        # ตำแหน่งของ Entry widgets
        english_label = tk.Label(add_window, text="คำศัพท์ภาษาอังกฤษ")
        thai_label = tk.Label(add_window, text="คำแปลภาษาไทย")
        type_label = tk.Label(add_window, text="ชนิดของคำ")

        # กำหนดตำแหน่งของ Entry widgets
        english_label.grid(row=0, column=0, padx=10, pady=10)
        english_entry.grid(row=0, column=1, padx=10, pady=10)

        thai_label.grid(row=1, column=0, padx=10, pady=10)
        thai_entry.grid(row=1, column=1, padx=10, pady=10)

        type_label.grid(row=2, column=0, padx=10, pady=10)
        type_entry.grid(row=2, column=1, padx=10, pady=10)

        # ปุ่มบันทึก
        save_btn = tk.Button(add_window, text="บันทึก", command=lambda: self.save_word(english_entry.get(), thai_entry.get(), type_entry.get(), add_window))
        save_btn.grid(row=3, columnspan=2, pady=10)

    def save_word(self, english, thai, word_type, add_window):
        # เพิ่มคำศัพท์ใหม่ลงใน self.words
        self.words.append({"English": english, "Thai": thai, "Type": word_type})

        # ปิดหน้าต่างเพิ่มคำศัพท์
        add_window.destroy()

        # แสดงคำศัพท์ทั้งหมด
        self.show_words()

    def delete_word(self):
        # ตรวจสอบว่าเลือกคำศัพท์ที่จะลบหรือไม่
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("คำเตือน", "กรุณาเลือกคำศัพท์ที่ต้องการลบ")
            return

        # ลบคำศัพท์จาก self.words
        for item in selected_item:
            english_word = self.tree.item(item, "values")[0]
            for word in self.words:
                if word["English"] == english_word:
                    self.words.remove(word)

        # แสดงคำศัพท์ที่เหลือ
        self.show_words()

    def search_word(self):
        # ดึงข้อมูลจาก Entry สำหรับค้นหา
        search_text = self.search_entry.get().lower()

        # สร้างรายการที่ตรงกับเงื่อนไขการค้นหา
        search_results = [word for word in self.words if search_text in word["English"].lower()]

        # ลบข้อมูลทั้งหมดในตาราง
        for record in self.tree.get_children():
            self.tree.delete(record)

        # แสดงคำศัพท์ที่ตรงกับการค้นหา
        for word in search_results:
            self.tree.insert("", "end", values=(word["English"], word["Thai"], word["Type"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()
