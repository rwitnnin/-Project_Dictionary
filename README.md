# -Project_Dictionary
![d1](https://github.com/rwitnnin/-Project_Dictionary/assets/150579607/ed0fbad1-92cd-4c54-a953-855922751557)
![d2](https://github.com/rwitnnin/-Project_Dictionary/assets/150579607/83498710-da39-4cf5-92b0-9c2eb8a7db38)
![d3](https://github.com/rwitnnin/-Project_Dictionary/assets/150579607/0afddb0e-49a7-41d6-9796-634b57466935)
![d4](https://github.com/rwitnnin/-Project_Dictionary/assets/150579607/ea746a54-9fa5-4ba6-ba3f-e095404de237)

โปรแกรมนี้เป็นตัวอย่างการใช้ Tkinter ใน Python เพื่อสร้าง GUI (Graphical User Interface) สำหรับแอปพลิเคชันพจนานุกรม. นอกจากนี้ยังมีการใช้โครงสร้างข้อมูลแบบ Dictionary ใน Python ในการจัดเก็บและจัดการคำศัพท์.
Tkinter GUI: โปรแกรมใช้ Tkinter เพื่อสร้าง GUI ที่ประกอบด้วยตาราง (Treeview) ที่แสดงคำศัพท์และปุ่มต่าง ๆ เพื่อเพิ่ม, ลบ, และค้นหาคำศัพท์.
Treeview Widget: ใช้ตาราง ttk.Treeview เพื่อแสดงคำศัพท์และรายละเอียด เช่น คำศัพท์ภาษาอังกฤษ, คำแปลภาษาไทย, และชนิดของคำ.
การใช้ Dictionary เป็นโครงสร้างข้อมูล: คำศัพท์ถูกจัดเก็บในรูปแบบของ Dictionaries ใน Python, ที่เก็บข้อมูลแบบ key-value pairs. ในที่นี้, key คือ "English", "Thai", และ "Type".
ฟังก์ชันสำหรับการเพิ่ม, ลบ, และค้นหาคำศัพท์: มีฟังก์ชันที่เป็น Method ของคลาส (add_word, delete_word, search_word) เพื่อให้ผู้ใช้สามารถทำการเพิ่มคำศัพท์, ลบคำศัพท์ที่เลือก, และค้นหาคำศัพท์ตามคำที่ระบุ.
การใช้ Toplevel เพื่อเพิ่มคำศัพท์: เมื่อผู้ใช้คลิกที่ปุ่ม "เพิ่มคำศัพท์", โปรแกรมจะสร้างหน้าต่าง Toplevel เพื่อให้ผู้ใช้กรอกข้อมูลใหม่สำหรับคำศัพท์.
การใช้ messagebox: ในกรณีที่ผู้ใช้ไม่ได้เลือกคำศัพท์ที่ต้องการลบ, โปรแกรมจะใช้ messagebox เพื่อแสดงข้อความเตือน.
การแสดงผลข้อมูล: ในท้ายที่สุด, โปรแกรมจะเรียก show_words เพื่อแสดงคำศัพท์ทั้งหมดในตาราง Treeview.

โครงสร้างข้อมูล
Dictionaries เป็นโครงสร้างข้อมูลที่ให้คุณเก็บข้อมูลในรูปแบบของคู่ (key, value) ใน Python คู่ของข้อมูลนี้เรียกว่า "key-value pairs" หรือ "รายการคีย์-ค่า" โดย Dictionaries จะมีลักษณะการใช้งานแบบไม่เรียงลำดับ (unordered) ซึ่งหมายความว่าคุณไม่สามารถรับประกันได้ว่าข้อมูลใน Dictionaries จะถูกเรียงลำดับเหมือนกับการประกาศค่าไว้หรือไม่
ซึ่งหมายความว่าไม่มีการจัดเรียงของข้อมูลตามลำดับของการเพิ่มข้อมูลลงไปใน Dictionary เหมือนกับ List หรือ Tuple ที่เป็นลำดับ
การสร้าง Dictionaries ใน Python ทำได้ด้วยการใช้วงเล็บปีกกา {} และระบุคู่ key-value ของข้อมูลภายในวงเล็บปีกกา
เลือกใช้เพราะ ง่ายต่อการการดึงข้อมูลด้วยคีย์ ให้ความสะดวกในการเพิ่ม, แก้ไข, และลบข้อมูล โดยใช้คีย์เพื่อระบุตำแหน่งข้อมูลที่ต้องการจัดการและสารมารถใช้คีย์เป็นตัวกลางในการค้นหาข้อมูล

Tkinter เป็นไลบรารีส่วนหนึ่งของ Python ที่ใช้สร้าง GUI (Graphical User Interface) หรือหน้าต่างกราฟิกในโปรแกรม โดย Tkinter มีลักษณะที่เข้าใจง่ายสำหรับผู้เริ่มต้น
คุณสมบัติหลักของ Tkinter:
ใช้งานง่าย: Tkinter เป็นไลบรารีที่เข้าใจง่ายและให้ผู้เรียนตัวเลือกที่ดีในการสร้าง GUI.
ติดตั้งและมีอยู่แทบทุกระบบปฏิบัติการ: Tkinter มีการติดตั้งมาพร้อมกับ Python ทั้งหมด, ไม่ต้องติดตั้งเพิ่ม.
หน้าต่างกราฟิกแบบหลายหน้าต่าง: สามารถสร้างหน้าต่างหลาย ๆ ที่สามารถเปิดพร้อมกันได้.
Widget หลากหลาย: มี Widget ต่าง ๆ ให้เลือกในการสร้างอินเทอร์เฟซผู้ใช้, เช่น Button, Label, Entry, Canvas, และอื่น ๆ.
การจัดการกับอินเทอร์เฟซผู้ใช้แบบอีเวนต์: สามารถตรวจจับเหตุการณ์ที่เกิดขึ้นจากผู้ใช้ เช่น การคลิกปุ่ม หรือการป้อนข้อมูล.
