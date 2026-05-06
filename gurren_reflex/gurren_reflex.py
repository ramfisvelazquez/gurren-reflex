import reflex as rx


FRASES_KAMINA = [
    "¡Quién diablos crees que soy!",
    "¡Cree en mí que cree en ti!",
    "¡Los imposibles son solo imposibles hasta que dejan de serlo!",
    "¡Perfora los cielos, Gurren Lagann!",
    "¡Tu espíritu brillará para siempre!",
    "¡Este taladro es el que perforará los cielos!",
]

PERSONAJES = [
    {"nombre": "Simon",     "rol": "El Perforador",      "color": "#00BFFF"},
    {"nombre": "Kamina",    "rol": "El Líder",            "color": "#FF4500"},
    {"nombre": "Yoko",      "rol": "La Francotiradora",   "color": "#FF1493"},
    {"nombre": "Nia",       "rol": "La Princesa",         "color": "#FFD700"},
    {"nombre": "Viral",     "rol": "El Rival Honorable",  "color": "#00FF7F"},
]


class State(rx.State):
    frase_idx: int = 0
    contador_clicks: int = 0
    personaje_sel: int = 0
    mostrar_spoiler: bool = False

    @rx.var
    def frase_actual(self) -> str:
        return FRASES_KAMINA[self.frase_idx % len(FRASES_KAMINA)]

    @rx.var
    def personaje_nombre(self) -> str:
        return PERSONAJES[self.personaje_sel]["nombre"]

    @rx.var
    def personaje_rol(self) -> str:
        return PERSONAJES[self.personaje_sel]["rol"]

    def siguiente_frase(self):
        self.frase_idx += 1
        self.contador_clicks += 1

    def seleccionar_personaje(self, idx: int):
        self.personaje_sel = idx

    def toggle_spoiler(self):
        self.mostrar_spoiler = not self.mostrar_spoiler


# ── Componentes ──────────────────────────────────────────────────────────────

def nav() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("⚙ GURREN LAGANN", weight="bold", size="4", color="#FF4500"),
            rx.spacer(),
            rx.text("PIERCE THE HEAVENS", size="2", color="#FFD700", weight="bold"),
            width="100%",
            padding_x="6",
            padding_y="3",
            align="center",
        ),
        background="rgba(0,0,0,0.85)",
        border_bottom="2px solid #FF4500",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
    )


def hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "TENGEN TOPPA",
                size="9",
                color="#FF4500",
                text_align="center",
                weight="bold",
            ),
            rx.heading(
                "GURREN LAGANN",
                size="9",
                color="#FFD700",
                text_align="center",
                weight="bold",
            ),
            rx.text(
                "天元突破グレンラガン",
                size="5",
                color="#AAAAAA",
                text_align="center",
            ),
            rx.divider(color_scheme="orange", size="4"),
            rx.text(
                "Una aplicación web desarrollada con Reflex y Python — "
                "tan imposible como perforar los cielos.",
                size="3",
                color="#CCCCCC",
                text_align="center",
                max_width="600px",
            ),
            spacing="4",
            align="center",
            padding_y="12",
        ),
        background="radial-gradient(ellipse at center, #1a0000 0%, #000000 70%)",
        border_bottom="2px solid #FF4500",
        width="100%",
        padding_x="6",
    )


def seccion_frase() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("💬 Frases de Kamina", size="6", color="#FFD700"),
            rx.text(
                "El líder de Equipo Gurren nunca pierde la fe. "
                "Haz clic para escuchar su sabiduría.",
                size="2",
                color="#888888",
            ),
            rx.box(
                rx.text(
                    State.frase_actual,
                    size="5",
                    weight="bold",
                    color="#FF4500",
                    text_align="center",
                ),
                background="rgba(255,69,0,0.08)",
                border="1px solid #FF4500",
                border_radius="8px",
                padding="6",
                width="100%",
                min_height="80px",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.hstack(
                rx.button(
                    "⚡ ¡Siguiente frase!",
                    on_click=State.siguiente_frase,
                    color_scheme="orange",
                    size="3",
                    radius="full",
                    variant="solid",
                ),
                rx.badge(
                    f"Clicks: {State.contador_clicks}",
                    color_scheme="amber",
                    size="2",
                    variant="surface",
                ),
                spacing="4",
                align="center",
            ),
            spacing="4",
            align="center",
        ),
        width="100%",
        padding="6",
        background="#0D0D0D",
        border="1px solid #FF4500",
    )


def tarjeta_personaje(idx: int, nombre: str, rol: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text("👤", size="7"),
            rx.heading(nombre, size="4", color="#FFD700"),
            rx.text(rol, size="2", color="#AAAAAA"),
            rx.button(
                "Seleccionar",
                on_click=State.seleccionar_personaje(idx),
                size="1",
                color_scheme="orange",
                variant="soft",
            ),
            spacing="2",
            align="center",
        ),
        padding="4",
        background="#0D0D0D",
        border="1px solid #333333",
        _hover={"border": "1px solid #FF4500"},
        cursor="pointer",
    )


def seccion_personajes() -> rx.Component:
    return rx.vstack(
        rx.heading("⚙ Equipo Gurren", size="7", color="#FFD700"),
        rx.text(
            f"Personaje seleccionado: {State.personaje_nombre} — {State.personaje_rol}",
            color="#FF4500",
            weight="bold",
            size="3",
        ),
        rx.grid(
            *[
                tarjeta_personaje(i, p["nombre"], p["rol"])
                for i, p in enumerate(PERSONAJES)
            ],
            columns="5",
            spacing="3",
            width="100%",
        ),
        spacing="4",
        align="center",
        width="100%",
    )


def seccion_spoiler() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("⚠ Zona de Spoilers", size="5", color="#FF4500"),
            rx.cond(
                State.mostrar_spoiler,
                rx.vstack(
                    rx.text(
                        "Kamina muere en el episodio 8, pero su espíritu vive "
                        "para siempre en Simon, quien se convierte en el "
                        "perforador más grande del universo.",
                        color="#CCCCCC",
                        text_align="center",
                    ),
                    rx.button(
                        "🙈 Ocultar spoiler",
                        on_click=State.toggle_spoiler,
                        color_scheme="red",
                        size="2",
                        variant="soft",
                    ),
                ),
                rx.button(
                    "👁 Mostrar spoiler",
                    on_click=State.toggle_spoiler,
                    color_scheme="orange",
                    size="2",
                ),
            ),
            spacing="3",
            align="center",
        ),
        padding="5",
        background="#0D0D0D",
        border="1px dashed #FF4500",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.divider(color_scheme="orange"),
            rx.text(
                "⚙ Hecho con Reflex + Python · Proyecto Académico 2025 · "
                "¡Quien diablos crees que soy! ⚙",
                size="1",
                color="#555555",
                text_align="center",
            ),
        ),
        padding="6",
        width="100%",
    )


# ── Página principal ─────────────────────────────────────────────────────────

def index() -> rx.Component:
    return rx.box(
        nav(),
        hero(),
        rx.box(
            rx.vstack(
                seccion_frase(),
                seccion_personajes(),
                seccion_spoiler(),
                spacing="8",
                width="100%",
                max_width="960px",
                padding_x="4",
                padding_y="8",
                align="center",
            ),
            display="flex",
            justify_content="center",
            width="100%",
        ),
        footer(),
        background="#050505",
        min_height="100vh",
        width="100%",
    )


app = rx.App(
    style={
        "background": "#050505",
        "font_family": "system-ui, sans-serif",
    }
)
app.add_page(index, title="Tengen Toppa — Mi Primera Web con Reflex")
