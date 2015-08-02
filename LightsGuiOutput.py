import tkinter as tk

class PiLights(tk.Frame):
    def __init__(self, lightStrings):
        self.root = tk.Tk()
        tk.Frame.__init__(self, self.root)
        # each label represents a string of lights
        self.labels = []
        
        for lightString in range(lightStrings):
            ls = tk.Label(self, text="  string " + str(lightString) + "  ", background="black", foreground="white")
            ls.pack(side="left", fill="both", expand=True)
            self.labels.append(ls)

        self.pack(fill="both", expand=True)
        self.update()

    def cleanup(self):
        pass

    def change(self, state, lightStrands):
        pinState = 0
        if state.lower() == 'on':
            pinState = 1
        for ls in lightStrands:
            ls = int(ls) - 1 # lists start at zero, we started out list at one
            if pinState == 1:
                self.labels[ls].configure(background="white", foreground="black")
            else:
                self.labels[ls].configure(background="black", foreground="white")
        self.update()


if __name__ == "__main__":
    pl = PiLights()
    #pl.flashAll(10, .1)
    pl.circleChase(10, .1)
    pl.cleanup()
