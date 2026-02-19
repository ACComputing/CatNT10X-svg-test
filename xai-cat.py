import tkinter as tk
import time
import random

class Windows11BlackBlueSim:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Windows 11 – Black Edition ♡")
        self.root.geometry("640x480")
        self.root.resizable(False, False)
        self.root.configure(bg='#000000')

        self.start_menu = None
        self.show_bios_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ─── BIOS ────────────────────────────────────────────────
    def show_bios_screen(self):
        self.clear_screen()
        canvas = tk.Canvas(self.root, width=640, height=480, bg="#000000", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        canvas.create_text(320, 50, text="American Megatrends", fill="#00FF00", font=("Courier", 16, "bold"))
        canvas.create_text(320, 85, text="BIOS Version 5.17.2026", fill="white", font=("Courier", 12))
        canvas.create_text(320, 115, text="Copyright (C) 2026 CatSDK Corp.", fill="#1E90FF", font=("Courier", 10))

        info_y = 170
        infos = [
            "Processor:  Intel(R) Core(TM) i9-14900K @ 6.00GHz",
            "Memory Test :  32768 MB OK",
            "NVMe Device(s) Detected",
            "USB Devices: Keyboard, Mouse",
            "",
            "Press [DEL] to enter SETUP",
            "Press [F11] for Boot Menu"
        ]

        for line in infos:
            canvas.create_text(60, info_y, text=line, fill="#00FF9D", anchor="w", font=("Courier", 12))
            info_y += 26

        progress = canvas.create_rectangle(80, 400, 80, 430, fill="#00FF9D", outline="")
        
        def animate():
            for x in range(80, 561, 10):
                canvas.coords(progress, 80, 400, x, 430)
                self.root.update()
                time.sleep(0.025)
            self.root.after(600, self.show_windows_boot)

        self.root.after(1400, animate)

    # ─── Boot Logo ───────────────────────────────────────────
    def show_windows_boot(self):
        self.clear_screen()
        canvas = tk.Canvas(self.root, width=640, height=480, bg="#000000", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        size = 38
        gap = 10
        x = 320 - size*2 - gap//2
        y = 160

        colors = ["#F25022", "#7FBA00", "#00A4EF", "#FFB900"]
        for i, color in enumerate(colors):
            cx = x + (i % 2) * (size + gap)
            cy = y + (i // 2) * (size + gap)
            canvas.create_rectangle(cx, cy, cx+size, cy+size, fill=color, outline="")

        canvas.create_text(320, 280, text="Windows 11", fill="white", font=("Segoe UI Variable", 40, "bold"))

        self.loading = canvas.create_text(320, 380, text="Starting up", fill="#4dabf7", font=("Segoe UI", 14))
        self.dots = 0

        def animate_dots():
            dots = "." * (self.dots % 4)
            canvas.itemconfig(self.loading, text=f"Starting up{dots}")
            self.dots += 1
            if self.dots < 24:
                self.root.after(260, animate_dots)
            else:
                self.root.after(700, self.show_desktop)

        animate_dots()

    # ─── Desktop ─────────────────────────────────────────────
    def show_desktop(self):
        self.clear_screen()

        canvas = tk.Canvas(self.root, width=640, height=432, bg="#00050F", highlightthickness=0)
        canvas.pack(fill="both", expand=False)

        # very subtle ambient glow (fixed for macOS~)
        canvas.create_oval(-400, -300, 1040, 800, fill="#0A1F38", stipple="gray25", outline="")

        icons = [
            ("This PC",       "💻", 40,  40),
            ("Recycle Bin",   "🗑️", 40, 140),
            ("Edge",          "🌐", 40, 240),
            ("Documents",     "📁", 40, 340),
        ]

        for name, emoji, x, y in icons:
            self._make_icon(canvas, x, y, emoji, name)

        # Taskbar ────────────────────────────────────────
        taskbar = tk.Frame(self.root, bg="#000000", height=52)
        taskbar.pack(side="bottom", fill="x")

        # Start button (black + blue accent)
        start = tk.Button(taskbar, text="❖", bg="#000000", fg="#0066CC",
                          activebackground="#1a1a2e", activeforeground="#3399FF",
                          font=("Segoe UI", 22), width=3, relief="flat",
                          command=self.toggle_start_menu)
        start.pack(side="left", padx=6, pady=6)

        # Search
        search = tk.Entry(taskbar, bg="#0F1C2E", fg="#88CCFF", font=("Segoe UI", 11),
                          width=30, relief="flat", insertbackground="white")
        search.insert(0, "   Type here to search")
        search.pack(side="left", padx=10, pady=8, ipady=5)

        # Clock
        self.clock = tk.Label(taskbar, text="12:34 PM", bg="#000000", fg="#e0e0ff",
                              font=("Segoe UI", 10))
        self.clock.pack(side="right", padx=16)
        self._update_clock()

        canvas.create_text(520, 100, text="double-click me~ nya", fill="#66AFFF",
                           font=("Segoe UI", 10, "italic"), angle=18)

    def _make_icon(self, canvas, x, y, emoji, name):
        frame = tk.Frame(self.root, bg="#000000", width=80, height=90)
        frame.place(x=x, y=y)

        lbl = tk.Label(frame, text=emoji, font=("Segoe UI", 36), bg="#000000")
        lbl.pack()

        txt = tk.Label(frame, text=name, fg="#d0e0ff", bg="#000000",
                       font=("Segoe UI", 9), wraplength=76, justify="center")
        txt.pack()

        def open_win(e=None):
            self._fake_window(name)
        lbl.bind("<Double-Button-1>", open_win)
        txt.bind("<Double-Button-1>", open_win)

    def _fake_window(self, title):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry(f"{random.randint(360,520)}x{random.randint(240,360)}+{random.randint(100,300)}+{random.randint(80,220)}")
        win.configure(bg="#0A1625")

        tb = tk.Frame(win, bg="#0052CC", height=36)
        tb.pack(fill="x")
        tk.Label(tb, text=title, bg="#0052CC", fg="white",
                 font=("Segoe UI", 11, "bold")).pack(side="left", padx=12, pady=6)

        body = tk.Frame(win, bg="#0A1625")
        body.pack(fill="both", expand=True)

        tk.Label(body, text=f"✦  welcome to fake {title}  ✦",
                 bg="#0A1625", fg="#00FFCC", font=("Segoe UI", 14)).pack(pady=60)

    def toggle_start_menu(self):
        if self.start_menu and self.start_menu.winfo_exists():
            self.start_menu.destroy()
            self.start_menu = None
            return

        rx = self.root.winfo_rootx()
        ry = self.root.winfo_rooty()
        self.start_menu = tk.Toplevel(self.root)
        self.start_menu.overrideredirect(True)
        self.start_menu.geometry(f"340x460+{rx+12}+{ry+self.root.winfo_height()-460-12}")
        self.start_menu.configure(bg="#000B1A")

        tk.Label(self.start_menu, text="Start", font=("Segoe UI", 17, "bold"),
                 bg="#000B1A", fg="#88DDFF").pack(anchor="w", padx=24, pady=14)

        apps = ["Settings", "File Explorer", "Store", "Photos", "Terminal", "Notepad++"]
        for app in apps:
            btn = tk.Button(self.start_menu, text=app, bg="#000000", fg="white",
                            activebackground="#003366", activeforeground="#66CCFF",
                            font=("Segoe UI", 12), relief="flat", anchor="w",
                            padx=24, pady=10)
            btn.pack(fill="x", padx=16, pady=2)
            btn.bind("<Button-1>", lambda e, a=app: self._launch(a))

    def _launch(self, name):
        if self.start_menu:
            self.start_menu.destroy()
            self.start_menu = None
        self._fake_window(name)

    def _update_clock(self):
        if not hasattr(self, 'clock') or not self.clock.winfo_exists():
            return
        self.clock.config(text=time.strftime("%I:%M %p"))
        self.root.after(15000, self._update_clock)


if __name__ == "__main__":
    print("  🐾  booting shadowy black & blue windows 11 ... mrrp~  💙🖤")
    app = Windows11BlackBlueSim()
    app.root.mainloop()
