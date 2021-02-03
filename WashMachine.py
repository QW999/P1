import random
import time


# 1 definim aria de responsabilitate la clasa mea
class WashMachine():
    "Responsabila de descrierea unei masine de spalat"

    timp_implicit = 10

    # 2. definim partile componente ale obiectului clasei
    def __init__(self, model, culoare, greutate_neta, volum_camera, volum_apa):
        ""
        self.model = model
        self.culoare = culoare
        self.greutate = greutate_neta
        self.volume = volum_camera
        self.volum_apa_max = volum_apa

        # 3. definim constante si limite in cadrul obiectului

        self.regim_spalare = [i for i in range(1, 11)]
        self.temp = 0
        self.rotations = 1500
        self.el_tens_max = 220
        self.volum_rufe_ocupat = 0
        self.volum_apa_ocupat = 0
        self.regim_curent = 0
        self.closed_door = False

    # 4. defimin functii posibile care o sa le expunem pentru utilizatorii clasei
    def __str__(self):
        "Definim reprezentarea string a obiectului clasei"
        string_pentru_printare = "Masina de spalat de model '{}'' de culoare {}.".format(self.model, self.culoare)
        return string_pentru_printare

    def electricitate_este_conectata(self):
        "este conexiune la electricitate"
        return True

    def apa_este_conectata(self):
        "este conexiune la apa"
        return True

    def camera_este_sigilata(self):
        "Verific daca usa de la camera de spalare e sigilata"
        return self.closed_door

    def regimul_este_selectat(self):
        "Verific ca regimul de spalate sa fie selectat"
        return self.regim_curent != 0

    def inchide_camera_spalare(self):
        self.closed_door = True

    def deschide_camera_spalare(self):
        self.closed_door = False

    def incarca_rufe(self, cant):
        "Incarcam o cantitate de rufe"
        if self.volum_rufe_ocupat < self.volume:
            self.volum_rufe_ocupat += cant
        else:
            print('capacitate maxima este atinsa')

    def select_regim(self, regim):
        'Selectam regimul de splare'
        if regim in self.regim_spalare:
            self.regim_curent = regim
        else:
            print('regim selectat nu exista')

    def pompeaza_apa(self):
        "pompam apa pina la cantitatea maxima admisibila"
        while True:
            c = random.randint(1, 2)
            print("Pompez apa : {} l".format(c))
            time.sleep(2)
            self.volum_apa_ocupat += c
            if self.volum_apa_ocupat >= self.volum_apa_max:
                break
        print('Am pompat per total {} l de apa'.format(self.volum_apa_ocupat))

    def print_wash_progress(self):
        "Printarea la procesul de spalare in terminal"
        overall_time = self.timp_implicit * self.regim_curent
        print('{}: Timpul de spalare necesar e {}.\nProcess bar:'.format(self.model, overall_time))
        while True:
            spent_time = random.randint(1, 3)
            overall_time = overall_time - spent_time
            print("*" * spent_time, end='')
            time.sleep(1)
            if overall_time <= 0:
                break
        print('\nSpalarea sa incheiat')

    def start_wash(self):
        "Metoda pentru a porni spararea propriuzisa"
        if self.apa_este_conectata() and self.electricitate_este_conectata() and self.camera_este_sigilata():
            if self.regimul_este_selectat():
                print("Am inceput lucrul")
                self.pompeaza_apa()
                self.print_wash_progress()
            else:
                print('Setari de regim incomplete')
        else:
            print('Conditiile necesare inceputului lucrului nu au fost intrunite')


# 5 testam implementarile din clasa noastra prin initializarea de obiecte si a metodelor acestora

m = WashMachine("Miele", "gri", 50, 7, 8)
print(m)
m.select_regim(10)
m.inchide_camera_spalare()
m.start_wash()