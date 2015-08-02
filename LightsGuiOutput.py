import tkinter as tk

class PiLights(tk.Frame):
    def __init__(self, lightStrings):
        self.root = tk.Tk()
        tk.Frame.__init__(self, self.root)
        # each label represents a string of lights
        self.labels = []
        
        for lightString in range(lightStrings):
            ls = tk.Label(self, text="ls" + str(lightString), background="black", foreground="white")
            ls.pack(side="left", fill="both", expand=True)
            self.labels.append(ls)

        self.pack(fill="both", expand=True)

    def cleanup(self):
        pass

    def change(self, state, leds):
        pinState = 0
        if state.lower() == 'on':
            pinState = 1
        for label in self.labels:
            if pinState == 1:
                label.configure(background="white", foreground="black")
            else:
                label.configure(background="white", foreground="black")


if __name__ == "__main__":
    pl = PiLights()
    #pl.flashAll(10, .1)
    pl.circleChase(10, .1)
    pl.cleanup()
