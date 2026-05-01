from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.card import MDCard
import datetime


class CardModulo(MDCard):
    pass


KV = '''
ScreenManager:
    PantallaCursos:
    PantallaQuiz:
    PantallaResultado:

<CardModulo>:
    size_hint_y: None
    height: "100dp"
    padding: 15
    radius: [20]
    elevation: 6
    md_bg_color: app.theme_cls.primary_color

    MDLabel:
        id: label
        text: ""
        halign: "center"
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style: "H6"


<PantallaCursos>:
    name: "cursos"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "🏀 Michael Jordan 23 Academy"
            md_bg_color: 0.8,0,0,1
            specific_text_color: 1,1,1,1

        ScrollView:
            MDBoxLayout:
                id: contenedor
                orientation: "vertical"
                padding: 20
                spacing: 15
                size_hint_y: None
                height: self.minimum_height


<PantallaQuiz>:
    name: "quiz"

    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 15

        MDProgressBar:
            id: barra
            value: 0

        MDLabel:
            id: pregunta
            halign: "center"
            font_style: "H6"

        MDRaisedButton:
            id: op1
            on_release: app.responder(0)

        MDRaisedButton:
            id: op2
            on_release: app.responder(1)

        MDRaisedButton:
            id: op3
            on_release: app.responder(2)


<PantallaResultado>:
    name: "resultado"

    MDBoxLayout:
        orientation: "vertical"
        padding: 30
        spacing: 20

        MDIcon:
            id: icono
            icon: "trophy"
            halign: "center"
            font_size: "100sp"

        MDLabel:
            id: resultado
            halign: "center"
            font_style: "H5"

        MDRaisedButton:
            text: "Generar Certificado 🏆"
            pos_hint: {"center_x": 0.5}
            on_release: app.generar_certificado()

        MDRaisedButton:
            text: "Volver"
            pos_hint: {"center_x": 0.5}
            on_release: app.volver()
'''


class PantallaCursos(Screen): pass
class PantallaQuiz(Screen): pass
class PantallaResultado(Screen): pass


class MiApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"

        self.puntaje = 0
        self.pregunta_actual = 0

        # 🏀 50 PREGUNTAS (5 MÓDULOS x 10)
        self.banco_preguntas = {

            "Jordan": [
                {"pregunta": "¿Quién es MJ?", "opciones": ["Jugador", "Coach", "Doctor"], "correcta": 0},
                {"pregunta": "Número?", "opciones": ["23", "10", "7"], "correcta": 0},
                {"pregunta": "Equipo?", "opciones": ["Bulls", "Lakers", "Heat"], "correcta": 0},
                {"pregunta": "País?", "opciones": ["USA", "México", "Brasil"], "correcta": 0},
                {"pregunta": "GOAT?", "opciones": ["Sí", "No", "Tal vez"], "correcta": 0},
                {"pregunta": "Campeonatos?", "opciones": ["6", "2", "10"], "correcta": 0},
                {"pregunta": "Liga?", "opciones": ["NBA", "FIFA", "NFL"], "correcta": 0},
                {"pregunta": "Retiro?", "opciones": ["Sí", "No", "Nunca"], "correcta": 0},
                {"pregunta": "Inspiración?", "opciones": ["Sí", "No", "Nada"], "correcta": 0},
                {"pregunta": "Leyenda?", "opciones": ["Sí", "No", "Tal vez"], "correcta": 0},
            ],

            "Dribbling": [
                {"pregunta": "Driblar?", "opciones": ["Botar", "Tirar", "Correr"], "correcta": 0},
                {"pregunta": "Control?", "opciones": ["Mano", "Pie", "Cabeza"], "correcta": 0},
                {"pregunta": "Sirve para?", "opciones": ["Avanzar", "Dormir", "Parar"], "correcta": 0},
                {"pregunta": "Cambio mano?", "opciones": ["Sí", "No", "Nunca"], "correcta": 0},
                {"pregunta": "Velocidad?", "opciones": ["Clave", "Nada", "Error"], "correcta": 0},
                {"pregunta": "Protección?", "opciones": ["Sí", "No", "Raro"], "correcta": 0},
                {"pregunta": "Agilidad?", "opciones": ["Alta", "Baja", "Nula"], "correcta": 0},
                {"pregunta": "MJ driblaba?", "opciones": ["Sí", "No", "Mal"], "correcta": 0},
                {"pregunta": "Dominio?", "opciones": ["Sí", "No", "Tal vez"], "correcta": 0},
                {"pregunta": "Control balón?", "opciones": ["Clave", "Error", "Nada"], "correcta": 0},
            ],

            "Tiro": [
                {"pregunta": "Tiro es?", "opciones": ["Lanzar", "Correr", "Saltar"], "correcta": 0},
                {"pregunta": "Objetivo?", "opciones": ["Canasta", "Defensa", "Pase"], "correcta": 0},
                {"pregunta": "Triple?", "opciones": ["3", "2", "1"], "correcta": 0},
                {"pregunta": "Libre?", "opciones": ["1", "2", "3"], "correcta": 0},
                {"pregunta": "Precisión?", "opciones": ["Clave", "Rara", "Error"], "correcta": 0},
                {"pregunta": "Equilibrio?", "opciones": ["Sí", "No", "Nada"], "correcta": 0},
                {"pregunta": "MJ tiraba?", "opciones": ["Sí", "No", "Poco"], "correcta": 0},
                {"pregunta": "Saltos?", "opciones": ["Sí", "No", "Nada"], "correcta": 0},
                {"pregunta": "Mano guía?", "opciones": ["Apoyo", "Principal", "Pie"], "correcta": 0},
                {"pregunta": "Tiro rápido?", "opciones": ["Sí", "No", "Nunca"], "correcta": 0},
            ],

            "Defensa": [
                {"pregunta": "Defensa?", "opciones": ["Evitar puntos", "Anotar", "Correr"], "correcta": 0},
                {"pregunta": "Robar?", "opciones": ["Steal", "Falta", "Gol"], "correcta": 0},
                {"pregunta": "Postura?", "opciones": ["Baja", "Alta", "Recta"], "correcta": 0},
                {"pregunta": "Zona?", "opciones": ["Área", "Jugador", "Nada"], "correcta": 0},
                {"pregunta": "Rebote?", "opciones": ["Control", "Error", "Gol"], "correcta": 0},
                {"pregunta": "Comunicación?", "opciones": ["Clave", "Inútil", "Raro"], "correcta": 0},
                {"pregunta": "Anticipar?", "opciones": ["Leer", "Dormir", "Correr"], "correcta": 0},
                {"pregunta": "Defensa gana?", "opciones": ["Sí", "No", "Tal vez"], "correcta": 0},
                {"pregunta": "MJ defendía?", "opciones": ["Sí", "No", "Nunca"], "correcta": 0},
                {"pregunta": "Presión?", "opciones": ["Alta", "Baja", "Nula"], "correcta": 0},
            ],

            "Leyenda": [
                {"pregunta": "MJ GOAT?", "opciones": ["Sí", "No", "Tal vez"], "correcta": 0},
                {"pregunta": "Campeonatos?", "opciones": ["6", "2", "10"], "correcta": 0},
                {"pregunta": "Bulls?", "opciones": ["Equipo", "País", "Liga"], "correcta": 0},
                {"pregunta": "Disciplina?", "opciones": ["Alta", "Baja", "Nula"], "correcta": 0},
                {"pregunta": "Mentalidad?", "opciones": ["Ganadora", "Débil", "Normal"], "correcta": 0},
                {"pregunta": "Trabajo duro?", "opciones": ["Clave", "Nada", "Raro"], "correcta": 0},
                {"pregunta": "Influencia?", "opciones": ["Global", "Local", "Nada"], "correcta": 0},
                {"pregunta": "Número 23?", "opciones": ["Icónico", "Raro", "Cualquiera"], "correcta": 0},
                {"pregunta": "Retiro?", "opciones": ["Sí", "No", "Nunca"], "correcta": 0},
                {"pregunta": "Inspiración?", "opciones": ["Sí", "No", "Tal vez"], "correcta": 0},
            ],
        }

        root = Builder.load_string(KV)
        self.crear_modulos(root)
        return root

    def crear_modulos(self, root):
        self.modulos = list(self.banco_preguntas.keys())
        cont = root.get_screen("cursos").ids.contenedor

        for m in self.modulos:
            c = CardModulo()
            c.ids.label.text = m
            c.bind(on_release=self.abrir_quiz)
            cont.add_widget(c)

    def abrir_quiz(self, card):
        self.modulo_actual = card.ids.label.text
        self.preguntas = self.banco_preguntas[self.modulo_actual]

        self.puntaje = 0
        self.pregunta_actual = 0

        self.root.current = "quiz"
        self.cargar()

    def cargar(self):
        p = self.preguntas[self.pregunta_actual]
        s = self.root.get_screen("quiz")

        s.ids.pregunta.text = p["pregunta"]
        s.ids.op1.text = p["opciones"][0]
        s.ids.op2.text = p["opciones"][1]
        s.ids.op3.text = p["opciones"][2]

        s.ids.barra.value = (self.pregunta_actual / len(self.preguntas)) * 100

    def responder(self, i):
        if i == self.preguntas[self.pregunta_actual]["correcta"]:
            self.puntaje += 1

        self.pregunta_actual += 1

        if self.pregunta_actual >= len(self.preguntas):
            self.resultado()
        else:
            self.cargar()

    def resultado(self):
        s = self.root.get_screen("resultado")

        if self.puntaje >= 8:
            s.ids.resultado.text = f"🏆 MJ APROBADO {self.puntaje}/10"
        else:
            s.ids.resultado.text = f"❌ INTENTA {self.puntaje}/10"

        self.root.current = "resultado"

    def generar_certificado(self):
        if self.puntaje < 8:
            return

        nombre = f"certificado_mj_{datetime.date.today()}.txt"

        with open(nombre, "w", encoding="utf-8") as f:
            f.write("🏀 MICHAEL JORDAN ACADEMY 🏀\n")
            f.write("CERTIFICADO DE FINALIZACIÓN\n")
            f.write(f"PUNTAJE: {self.puntaje}/10\n")
            f.write(f"FECHA: {datetime.date.today()}\n")
            f.write("LEYENDA DEL BASKETBALL 🐐\n")

        print("Certificado creado:", nombre)

    def volver(self):
        self.root.transition = SlideTransition(direction="right")
        self.root.current = "cursos"


if __name__ == "__main__":
    MiApp().run()