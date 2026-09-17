from fpdf import FPDF

class Shirtificate(FPDF):

    def __init__(self):

        super().__init__(orientation = "P", unit = "mm", format = "A4")

        self.add_page()

        self.set_auto_page_break(auto = False)

    def header(self):
        self.set_font("helvetica", "B", 45)

        self.set_y(40)

        self.cell(0, 10, "CS50 Shirtificate", align = "C")


    def add_shirt(self, username):
        self.image("shirtificate.png", x = 20, y = 80, w = 170)

        self.set_font("helvetica", "B", 24)

        self.set_text_color(255,255,255)


        self.set_y(140)

        self.cell(0, 10, f"{username} took CS50", align = "C")

def main():
    name = input("Name: ").strip()

    pdf = Shirtificate()

    pdf.add_shirt(name)

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()






